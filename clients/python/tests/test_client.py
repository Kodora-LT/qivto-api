import unittest

from qivto import QivtoClient


class FakeResponse:
    status = 200

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return b'{"values":["example"]}'


class ClientTest(unittest.TestCase):
    def test_uuid_request(self):
        captured = {}

        def transport(request, timeout):
            captured["request"] = request
            captured["timeout"] = timeout
            return FakeResponse()

        client = QivtoClient(transport=transport)
        self.assertEqual(client.uuid(3), {"values": ["example"]})
        self.assertEqual(captured["request"].method, "POST")
        self.assertEqual(captured["request"].data, b'{"count": 3}')
        self.assertEqual(captured["timeout"], 20.0)


if __name__ == "__main__":
    unittest.main()
