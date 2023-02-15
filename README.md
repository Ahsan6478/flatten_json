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
