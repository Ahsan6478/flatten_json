"""Export flattened JSON data to various formats."""

import pandas as pd

from .core import flatten


def to_dataframe(data):
    """Flatten JSON data and return a pandas DataFrame.

    Args:
        data: A JSON-compatible Python object (dict, list, etc.).

    Returns:
        A pandas DataFrame with flattened columns.
    """
    flat = flatten(data)
    return pd.DataFrame(flat)
