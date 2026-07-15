import argparse
from qivto import QivtoClient

parser = argparse.ArgumentParser(description="Generate UUID v4 values using QIVTO")
parser.add_argument("count", nargs="?", type=int, default=1)
args = parser.parse_args()

for value in QivtoClient().uuid(args.count)["values"]:
    print(value)
print("\nBuilt with QIVTO API: https://qivto.com/en/api")
