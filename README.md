# PrettyPrint

PrettPrint is a library for various formatters and beautifiers.

It currently hosts a simple routine, `obj2str` that converts a Python object into a JSON-like string. It was written while working with heavily nested Python objects to make it easier to visualize the results.

It is similar to json.dumps() without the constraints that the object be JSON serializable. It will output any Python object by recursively traversing through all its values, formatting the data types it recognizes into JSON-like format and writing out all others as strings.

For JSON-serializable objects it will output the same string as json.dumps().

## Features
* Configurable tab string.
* Recognized Python data types: `dict`, `list`, `bool`, `str`, `int`, `float`, `None`.
  * All other data types are simply rendered as a string, so any Python object will be handled.
  * For JSON-serializable objects, it will output the same string as json.dumps() with the appropriate parameter settings.

## Installation

Install from the credxai GitHub repository:

```
python -m pip install git+https://github.com/credx-ai/credxai-utilities-prettyprint.git
```

See the [pip install](https://pip.pypa.io/en/stable/cli/pip_install/) documentation for other forms of this command if you need a specific branch or tag.

## Usage

The following Python session gives an example of how it works:

```python
>>> from credxai.utilities import prettyprint as pp

>>> d = {"str": "hello", "int": 1, "dict": { "list": [1, 2, 3], "tuple": (1, 2, 3), "set": {1, 2, 3}}, "bool": True, "null": None, "range": range(2) }

>>> print(pp.obj2str(d))
{
  "str": "hello",
  "int": "1",
  "dict": {
    "list": [
      "1",
      "2",
      "3"
    ],
    "tuple": "(1, 2, 3)",
    "set": "{1, 2, 3}"
  },
  "bool": true,
  "null": null,
  "range": "range(0, 2)"
}

>>> print(pp.obj2str(d, "|__"))
{
|__"str": "hello",
|__"int": "1",
|__"dict": {
|__|__"list": [
|__|__|__"1",
|__|__|__"2",
|__|__|__"3"
|__|__],
|__|__"tuple": "(1, 2, 3)",
|__|__"set": "{1, 2, 3}"
|__},
|__"bool": true,
|__"null": null,
|__"range": "range(0, 2)"
}
>>>
```

The package currently exposes a single function called `obj2str`:

```python
def obj2str(obj: object, tab: str = "  ") -> str:
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
```

## Contributing

Pull requests, bug reports, feature suggestions, and other forms of contribution are welcome!

For major changes, please open an issue or Jira ticket to discuss what you would like to change.

## Contact
mauricio.lomelin@credx.ai