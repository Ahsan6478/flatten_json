from .core import flatten, flatten_json, flatten_single

__version__ = "0.1.0"
__all__ = [
    "flatten",
    "flatten_json",
    "flatten_single",
    "to_csv",
    "to_excel",
    "to_dataframe",
]


def to_csv(data, file_name):
    """Flatten JSON data and export to CSV. Requires pandas."""
    from .export import to_csv as _to_csv
    return _to_csv(data, file_name)


def to_excel(data, file_name):
    """Flatten JSON data and export to Excel. Requires pandas and xlsxwriter."""
    from .export import to_excel as _to_excel
    return _to_excel(data, file_name)


def to_dataframe(data):
    """Flatten JSON data and return a pandas DataFrame. Requires pandas."""
    from .export import to_dataframe as _to_dataframe
    return _to_dataframe(data)
