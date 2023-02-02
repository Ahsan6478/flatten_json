"""Core JSON flattening logic."""


def _is_scalar(value):
    """Check if a value is a scalar (not a dict or list)."""
    return not isinstance(value, (dict, list))


def _flatten_dict(dict_key, data, c_str=None):
    """Flatten a nested dictionary within a parent container."""
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
    """Flatten a nested list within a parent container."""
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
