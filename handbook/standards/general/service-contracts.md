# Service Contract Changes

Before editing behavior that crosses service or repository boundaries, identify its actual caller,
public entrypoint, data owner, and downstream consumers. Use the observed route, message, or shared
package contract to locate the owner; a repository name alone is insufficient evidence.

For HTTP, proxy, event, queue, webhook, schema, or shared-package changes, inspect both producers
and consumers. Preserve compatibility while old and new versions may run together. When several
repositories change, define a safe deployment order and verify each changed side with its own
project checks. A passing test suite in one service does not establish consumer compatibility.
