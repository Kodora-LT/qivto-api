# cURL examples

Status:

```bash
curl --fail-with-body https://qivto.com/api/v1/status
```

Tool catalog:

```bash
curl --fail-with-body "https://qivto.com/api/v1/tools?lang=en"
```

UUID values:

```bash
curl --fail-with-body -X POST https://qivto.com/api/v1/uuid \
  -H "Content-Type: application/json" \
  -d '{"count":3}'
```

SHA-256 hash:

```bash
curl --fail-with-body -X POST https://qivto.com/api/v1/hash \
  -H "Content-Type: application/json" \
  -d '{"algorithm":"sha256","text":"QIVTO"}'
```

Format JSON:

```bash
curl --fail-with-body -X POST https://qivto.com/api/v1/json-format \
  -H "Content-Type: application/json" \
  -d '{"json":{"project":"QIVTO","active":true}}'
```
