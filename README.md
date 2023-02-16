# flatten-json-util

Recursively flatten nested JSON structures (dicts and lists) into flat dictionaries with compound underscore-separated keys.

## Installation

```bash
pip install .
```

Or install in development mode:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from flatten_json_util import flatten

# Flatten a nested dict
data = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "New York",
            "zip": "10001"
        },
        "scores": [95, 87, 92]
    }
}

result = flatten(data)
# [{'user_name': 'Alice', 'user_address_city': 'New York', 'user_address_zip': '10001',
#   'user_scores_0': 95, 'user_scores_1': 87, 'user_scores_2': 92}]
```

## API

### `flatten(data)`

The main entry point. Accepts a dict or a list of dicts and returns a list of flat dictionaries.

```python
# Single dict
flatten({"a": {"b": 1}})
# [{'a_b': 1}]

# List of dicts
flatten([{"a": {"b": 1}}, {"a": {"b": 2}}])
# [{'a_b': 1}, {'a_b': 2}]
```

### `flatten_single(data)`

Flatten a single dict or list into one flat dictionary. Returns a one-element list.

```python
from flatten_json_util import flatten_single

flatten_single({"x": {"y": "z"}})
# [{'x_y': 'z'}]
```

### `flatten_json(data)`

Flatten a dict-of-dicts where each top-level key is a record identifier.

```python
from flatten_json_util import flatten_json

data = {
    "record1": {"name": "Alice", "info": {"age": 30}},
    "record2": {"name": "Bob", "info": {"age": 25}},
}
flatten_json(data)
# [{'name': 'Alice', 'info_age': 30}, {'name': 'Bob', 'info_age': 25}]
```

### Export Functions

Export flattened data directly to CSV, Excel, or a pandas DataFrame:

```python
from flatten_json_util import to_csv, to_excel, to_dataframe

data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}

# Export to CSV
to_csv(data, "output")       # creates output.csv

# Export to Excel
to_excel(data, "output")     # creates output.xlsx

# Get a pandas DataFrame
df = to_dataframe(data)
```

## Supported Value Types

All JSON-compatible Python types are handled:
- `str`, `int`, `float`, `bool`, `None` -- kept as leaf values
- `dict` -- recursively flattened with underscore-joined keys
- `list` -- elements indexed by position (0, 1, 2, ...)

## Running Tests

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT
