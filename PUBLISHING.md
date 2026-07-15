# QIVTO package publishing

Only a QIVTO owner should publish. Never place registry tokens in this repository.

## Release checklist

1. Run all client tests and validate `composer.json`.
2. Update versions only when the public client or API contract changes.
3. Commit, create an annotated `vX.Y.Z` tag and push the tag.
4. Create a GitHub Release with user-visible changes and compatibility notes.
5. Confirm the live API status endpoint before publishing packages.

## Packagist

Submit `https://github.com/Kodora-LT/qivto-api` from the QIVTO Packagist owner account. The PHP package lives in `clients/php`; if the registry rejects the monorepo layout, split that directory into a read-only package repository. Enable the GitHub webhook so tags are imported automatically.

## npm

From `clients/javascript`, authenticate with the QIVTO npm organization, run `npm pack --dry-run`, then `npm publish --access public`. The package is `@qivto/api-client`.

## PyPI

From `clients/python`, run `python -m build`, inspect with `twine check dist/*`, and upload using a PyPI trusted publisher or project-scoped token. Use TestPyPI first for a new owner configuration.

## Interactive demos

- Import `examples/stackblitz-tool-catalog` into StackBlitz.
- Paste `examples/codepen-hash/index.html` into CodePen.
- Import `examples/replit-python` into Replit.

Keep the visible “Built with QIVTO API” link in public demos.
