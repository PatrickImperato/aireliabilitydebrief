import json
import sys
from jsonschema import Draft202012Validator

def loadJson(path):
    with open(path, "r", encoding="utf 8") as f:
        return json.load(f)

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python validateJson.py schema.json file.json")

    schema = loadJson(sys.argv[1])
    doc = loadJson(sys.argv[2])

    validator = Draft202012Validator(schema)
    errors = list(validator.iter_errors(doc))

    if errors:
        errors.sort(key=lambda e: list(e.path))
        for err in errors:
            path = ".".join([str(p) for p in err.path])
            print(path + " " + err.message)
        raise SystemExit(1)

    print("Validation passed")

main()
