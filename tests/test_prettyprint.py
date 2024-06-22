# Steps to set up and run this test module:
#   $ python -m pip install pytest
#   $ python -m pip install -e .
# Run all tests
#   $ pytest tests/test_prettyprint.py
# Run a specific test case (-k) in verbose mode (-v, -vv, -vvv, ...)
#   $ pytest -vv tests/test_prettyprint.py -k test_obj2str
# More info: https://docs.pytest.org/en/stable/contents.html

import json
import pytest
from credxai.utilities.prettyprint import obj2str

def test_obj2str():

    # Strings
    d = "string"
    assert d == json.loads(obj2str(d))
    d = " spaces and more spaces  "
    assert d == json.loads(obj2str(d))
    # For this next test case, we cannot use json.dumps() because:
    #   1) a string is not a JSON object, so json.loads() will fail
    #   2) newlines are a control character and must be escaped (https://www.ietf.org/rfc/rfc4627.txt)
    # We expect the output to simply be the input wrapped in double quotes
    d = "\nnew \n lines\n"
    assert f"\"{d}\"" == obj2str(d)

    d = "| special characters: ''!@#$%^&*()_+"
    assert d == json.loads(obj2str(d))

    # Boolean
    d = True
    assert d == json.loads(obj2str(d))
    d = False
    assert d == json.loads(obj2str(d))

    # None
    d = None
    assert d == json.loads(obj2str(d))

    # List
    d = [1, 2, 3]
    assert d == json.loads(obj2str(d))
    d = [1, "2", "three", "4", None, True, False]
    assert d == json.loads(obj2str(d))

    # Dict
    d = {"key": "value"}
    assert d == json.loads(obj2str(d))
    d = {"key": "value", "int": 1, "float": 1.0, "bool": True, "none": None, "list": [1, 2, 3], "dict": {"key": "value"}}
    assert d == json.loads(obj2str(d))

    # Byte
    d = b"bytes",
    assert d != json.loads(obj2str(d)) # Byte not supported
    d = {"key": b"bytes"},
    assert d != json.loads(obj2str(d)) # Byte not supported

    # Raw
    d = r"raw",
    assert d != json.loads(obj2str(d)) # Raw not supported
    d = {"raw": r"raw"},
    assert d != json.loads(obj2str(d)) # Raw not supported

    # Tuples
    d = (1, 2, 3)
    assert d != json.loads(obj2str(d)) # Tuples are not supported
    d = {"tuple": (1, 2, 3)}
    assert d != json.loads(obj2str(d)) # Tuples are not supported
    d = {"tuple": (1, "2", "three", "4", None, True, False)}
    assert d != json.loads(obj2str(d)) # Tuples are not supported