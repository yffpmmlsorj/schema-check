# schema-check

A small validator for a useful subset of JSON Schema.

## Why

Mostly written for my own projects, but it may be useful to someone else.

## Install

```bash
pip install schema-check
```

## Usage

```python
from schema_check import schemaCheck

result = schemaCheck("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
