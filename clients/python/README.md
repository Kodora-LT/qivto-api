# Python client

```python
from qivto import QivtoClient

qivto = QivtoClient()
print(qivto.tools("en"))
```

Install the local package with `pip install -e .`. Run tests with `PYTHONPATH=src python -m unittest discover -s tests`.

The client uses only the Python standard library and has no runtime dependencies.
