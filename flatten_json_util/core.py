"""Core JSON flattening logic."""


def _is_scalar(value):
    """Check if a value is a scalar (not a dict or list)."""
    return not isinstance(value, (dict, list))
