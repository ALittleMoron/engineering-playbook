from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROFILE_NAME_PATTERN = re.compile(r"[a-z][a-z0-9-]*")
PROFILE_KEYS = {
    "schema_version",
    "name",
    "version",
    "description",
    "use_cases",
    "fragments",
}


class ProfileError(ValueError):
    pass


@dataclass(frozen=True)
class Profile:
    name: str
    version: str
    description: str
    use_cases: tuple[str, ...]
    fragments: tuple[Path, ...]
    manifest_path: Path


def _require_non_empty_string(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ProfileError(f"{key} must be a non-empty string")
    return value


def _require_string_list(data: dict[str, Any], key: str) -> tuple[str, ...]:
    value = data.get(key)
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(item, str) or not item.strip() for item in value)
    ):
        raise ProfileError(f"{key} must be a non-empty list of non-empty strings")
    return tuple(value)


def _path_within(candidate: Path, directory: Path) -> bool:
    try:
        candidate.relative_to(directory)
    except ValueError:
        return False
    return True


def load_profile(repository: Path, name: str) -> Profile:
    if PROFILE_NAME_PATTERN.fullmatch(name) is None:
        raise ProfileError(f"invalid profile name: {name!r}")

    profiles_directory = (repository / "agents" / "profiles").resolve()
    manifest_path = profiles_directory / f"{name}.toml"
    if not manifest_path.is_file():
        raise ProfileError(f"profile does not exist: agents/profiles/{name}.toml")
    if not _path_within(manifest_path.resolve(), profiles_directory):
        raise ProfileError(f"profile is outside agents/profiles: {name}")

    try:
        with manifest_path.open("rb") as manifest_file:
            data = tomllib.load(manifest_file)
    except tomllib.TOMLDecodeError as error:
        raise ProfileError(f"invalid TOML in agents/profiles/{name}.toml: {error}") from error

    unknown_keys = set(data) - PROFILE_KEYS
    if unknown_keys:
        keys = ", ".join(sorted(unknown_keys))
        raise ProfileError(f"unknown profile keys in {name}: {keys}")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ProfileError("schema_version must be the integer 1")

    profile_name = _require_non_empty_string(data, "name")
    if profile_name != name:
        raise ProfileError(f"profile name {profile_name!r} must match filename {name!r}")
    version = _require_non_empty_string(data, "version")
    description = _require_non_empty_string(data, "description")
    use_cases = _require_string_list(data, "use_cases")
    fragment_names = _require_string_list(data, "fragments")
    if len(fragment_names) != len(set(fragment_names)):
        raise ProfileError(f"profile {name} contains duplicate fragments")

    fragments_directory = (repository / "agents" / "fragments").resolve()
    fragments: list[Path] = []
    for fragment_name in fragment_names:
        relative_path = Path(fragment_name)
        candidate = (fragments_directory / relative_path).resolve()
        if relative_path.is_absolute() or not _path_within(candidate, fragments_directory):
            raise ProfileError(
                f"fragment path is outside agents/fragments: {fragment_name}"
            )
        if candidate.suffix != ".md" or not candidate.is_file():
            raise ProfileError(f"fragment does not exist: {fragment_name}")
        if not candidate.read_text(encoding="utf-8").strip():
            raise ProfileError(f"fragment is empty: {fragment_name}")
        fragments.append(candidate)

    return Profile(
        name=profile_name,
        version=version,
        description=description,
        use_cases=use_cases,
        fragments=tuple(fragments),
        manifest_path=manifest_path,
    )


def render_profile(repository: Path, profile: Profile) -> str:
    fragments_directory = (repository / "agents" / "fragments").resolve()
    fragment_documents: list[str] = []
    digest = hashlib.sha256()
    metadata = {
        "name": profile.name,
        "version": profile.version,
        "description": profile.description,
        "use_cases": profile.use_cases,
    }
    digest.update(
        json.dumps(metadata, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )

    for fragment in profile.fragments:
        relative_path = fragment.relative_to(fragments_directory).as_posix()
        content = fragment.read_text(encoding="utf-8").rstrip("\n")
        digest.update(b"\0")
        digest.update(relative_path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(content.encode("utf-8"))
        fragment_documents.append(content)

    manifest = profile.manifest_path.relative_to(repository).as_posix()
    header = (
        f"<!-- Generated by scripts/build-agents from {manifest}. "
        "Do not edit directly. -->\n"
        f"<!-- Profile: {profile.name}; version: {profile.version}; "
        f"source-sha256: {digest.hexdigest()} -->"
    )
    body = "\n\n".join(fragment_documents)
    return f"{header}\n\n{body}\n"


def output_path(repository: Path, profile: Profile) -> Path:
    return repository / "agents" / "dist" / profile.name / "AGENTS.md"


def write_if_changed(path: Path, content: str) -> bool:
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as output_file:
            output_file.write(content)
            output_file.flush()
            os.fsync(output_file.fileno())
        os.chmod(temporary_path, 0o644)
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)
    return True


def available_profiles(repository: Path) -> tuple[str, ...]:
    profiles_directory = repository / "agents" / "profiles"
    return tuple(path.stem for path in sorted(profiles_directory.glob("*.toml")))
