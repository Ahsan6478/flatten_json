"""Export flattened JSON data to various formats.

Provides functions to convert nested JSON data directly
to CSV, Excel, or pandas DataFrame output.
"""

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


def to_csv(data, file_name):
    """Flatten JSON data and export to a CSV file.

    Args:
        data: A JSON-compatible Python object.
        file_name: Output file path (without extension).
    """
    df = to_dataframe(data)
    df.to_csv(f"{file_name}.csv", index=False)


def to_excel(data, file_name):
    """Flatten JSON data and export to an Excel file.

    Args:
        data: A JSON-compatible Python object.
        file_name: Output file path (without extension).
    """
    df = to_dataframe(data)
    with pd.ExcelWriter(
        f"{file_name}.xlsx",
        engine="xlsxwriter",
        engine_kwargs={"options": {"strings_to_urls": False}},
    ) as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)
