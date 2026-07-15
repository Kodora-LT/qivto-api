import json
import urllib.request

request = urllib.request.Request(
    "https://qivto.com/api/v1/uuid",
    data=json.dumps({"count": 5}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(request, timeout=10) as response:
    data = json.load(response)
for value in data.get("uuids", []):
    print(value)
print("\nBuilt with QIVTO API: https://qivto.com/en/api")
