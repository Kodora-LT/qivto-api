# QIVTO API

Official open-source clients, examples and OpenAPI specification for the free [QIVTO Public API](https://qivto.com/en/api).

## Available endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/tools?lang=en` | List active QIVTO tools |
| POST | `/uuid` | Generate 1–100 UUID v4 values |
| POST | `/hash` | Hash text up to 1 MB |
| POST | `/json-format` | Validate and format JSON |
| GET | `/status` | Read API health and version |

Base URL: `https://qivto.com/api/v1`  
Authentication: not required  
Public limit: 60 requests per minute per session

## Clients

- [PHP client](clients/php/README.md)
- [JavaScript client](clients/javascript/README.md)
- [Python client](clients/python/README.md)
- [cURL examples](examples/curl/README.md)
- [OpenAPI 3.1 specification](openapi.yaml)

## Mini projects

- `examples/browser-tool-catalog` – searchable tool catalog in a single HTML file.
- `examples/php-hash` – minimal PHP hash form using the public API.
- `examples/python-uuid` – command-line UUID generator.

## Error handling

All errors use JSON with an `error` property. A `422` response means invalid input; `429` means the public minute limit was exceeded. Read `Retry-After` before retrying.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Report security issues privately using [SECURITY.md](SECURITY.md), not through a public issue.

## License

MIT. See [LICENSE](LICENSE).
