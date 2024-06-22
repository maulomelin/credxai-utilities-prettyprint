# TODO: Document the encoding/decoding tables for the mappers.

def obj22str(obj: object, tab: str = "  ") -> str:
    """Converts a Python object into a pretty-printable JSON string.

    This function is a wrapper around the _encode() function, which is a
    recursive function that translates a Python object into a JSON-like string.

    It is similar to json.dumps() without the constraints that the object
    be JSON serializable. It will pretty-print any Python object, formatting
    data types it recognizes in JSON-like format, and all others as strings.

    For JSON-serializable objects, it will output the same string as json.dumps().

    Parameters:
        obj (object): A Python object to JSON-ify into a pretty-printable string.
        tab (str): The tab character to use for indentation.

    Returns:
        str: The pretty-printed string.
    """
    return _encode(obj, tab, 0)

def _encode(obj: object, tab: str = "  ", n: int = 0) -> str:
    """Translates a Python object into a JSON-like string.

    This is designed to be a recursive function that translates a
    Python object into a JSON-like string. It will format any data
    types it recognizes in JSON-like format, and all others as strings.

    Parameters:
        obj (object): A Python object to pretty-print.
        tab (str): The tab character to use for indentation.
        n (int): The current level of indentation.
            Internal parameter used for recursion.

    Returns:
        str: The pretty-printed string.
    """
    if isinstance(obj, dict):
        out = f"{{\n"
        empty = True
        for key, value in obj.items():
            out += f'{tab * (n+1)}"{key}": {_encode(obj=value, tab=tab, n=n + 1)},\n'
            empty = False
        if not empty:
            out = out[:-2] + f"\n{tab * n}}}"  # Remove the last comma
        else:
            out = out[:-1] + f"{tab * n}}}"  # Remove the last comma
    elif isinstance(obj, list):
        out = f"[\n"
        empty = True
        for value in obj:
            out += f"{tab * (n+1)}{_encode(obj=value, tab=tab, n=n + 1)},\n"
            empty = False
        if not empty:
            out = out[:-2] + f"\n{tab * n}]"  # Remove the last comma
        else:
            out = out[:-1] + f"{tab * n}]"  # Remove the last comma
    elif isinstance(obj, bool):
        if obj == True:
            out = "true"
        else:
            out = "false"
    elif isinstance(obj, str):
        out = f'"{obj}"'
    elif isinstance(obj, int) or isinstance(obj, float):
        out = obj
    elif obj is None:
        out = "null"
    else:
        out = f'"{obj}"'
    return out