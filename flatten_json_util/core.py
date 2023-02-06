"""Core JSON flattening logic.

Recursively flattens nested JSON structures (dicts and lists) into
flat dictionaries with compound keys separated by underscores.
"""


def _is_scalar(value):
    """Check if a value is a scalar (not a dict or list)."""
    return not isinstance(value, (dict, list))


def _flatten_dict(dict_key, data, c_str=None):
    """Flatten a nested dictionary within a parent container.

    Args:
        dict_key: The key in ``data`` that points to the dict to flatten.
        data: The parent container (dict or list).
        c_str: Accumulated prefix string for key naming.

    Returns:
        A flat dictionary with compound keys.
    """
    result = {}
    if dict_key is None:
        dict_key = ""
    for i_key in data[dict_key].keys():
        value = data[dict_key][i_key]
        if c_str:
            prefix = f"{c_str}_{dict_key}"
        else:
            prefix = str(dict_key)

        if isinstance(value, dict):
            result.update(_flatten_dict(i_key, data[dict_key], c_str=prefix))
        elif isinstance(value, list):
            result.update(_flatten_list(data[dict_key], i_key, c_str=prefix))
        else:
            result[f"{prefix}_{i_key}"] = value

    return result


def _flatten_list(data, dict_key=None, c_str=None):
    """Flatten a nested list within a parent container.

    Args:
        data: The parent container (dict or list).
        dict_key: The key in ``data`` that points to the list to flatten.
            If ``None``, ``data`` itself is treated as the list.
        c_str: Accumulated prefix string for key naming.

    Returns:
        A flat dictionary with compound keys.
    """
    result = {}
    if dict_key is None:
        dict_key = ""
        items = data
    else:
        items = data[dict_key]

    for num in range(len(items)):
        value = items[num]
        if c_str:
            prefix = f"{c_str}_{dict_key}"
        else:
            prefix = str(dict_key)

        if isinstance(value, dict):
            result.update(_flatten_dict(num, items, c_str=prefix))
        elif isinstance(value, list):
            result.update(_flatten_list(items, num, c_str=prefix))
        else:
            result[f"{prefix}_{num}"] = value

    return result


def flatten_single(data):
    """Flatten a single JSON object (dict or list) into a flat dictionary.

    Args:
        data: A dict or list to flatten.

    Returns:
        A list containing one flat dictionary.

    Example:
        >>> flatten_single({"a": {"b": 1, "c": 2}})
        [{'a_b': 1, 'a_c': 2}]
    """
    result = {}
    if isinstance(data, dict):
        for key in data.keys():
            if isinstance(data[key], dict):
                result.update(_flatten_dict(key, data))
            elif isinstance(data[key], list):
                result.update(_flatten_list(data, key))
            else:
                result[key] = data[key]
    elif isinstance(data, list):
        result.update(_flatten_list(data))
    return [result]


def flatten_json(data):
    """Flatten a dictionary of records into a list of flat dictionaries.

    Expects ``data`` to be a dict where each value is itself a dict
    representing one record.

    Args:
        data: A dict of dicts (e.g. ``{"record1": {...}, "record2": {...}}``).

    Returns:
        A list of flat dictionaries, one per record.

    Example:
        >>> flatten_json({"r1": {"name": "Alice", "addr": {"city": "NY"}}})
        [{'name': 'Alice', 'addr_city': 'NY'}]
    """
    results = []
    for key in data:
        record = data[key]
        flat = {}
        for field in record.keys():
            value = record[field]
            if isinstance(value, dict):
                flat.update(_flatten_dict(field, record))
            elif isinstance(value, list):
                flat.update(_flatten_list(record, field))
            else:
                flat[field] = value
        results.append(flat)
    return results
