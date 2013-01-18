"""Methods that can be used on pyrays"""
import pyray
import string

CASE_LOWER = 0
CASE_UPPER = 1

def array_keys(array, search_value=None):
    """array_keys() returns the keys, numeric and string, from the input array.

    If the optional search_value is specified, then only the keys for that
    value are returned. Otherwise, all the keys from the input are returned.
    """
    keys = pyray.Pyray()

    if not search_value:
        keys.extend(array.keys())
    else:
        keys.extend([x[0] for x in array.items() if [1] == search_value])
    return keys

def array_change_key_case(array, case=CASE_LOWER):
    """Returns an array with all keys from array
    lowercased or uppercased.  Numbered indices are left as is.
    """
    keys = pyray.Pyray()

    if case == CASE_LOWER:
        func = string.lower
    else:
        func = string.upper

    keys.extend([func(x) for x in array.keys() if isinstance(basestring, x)])
    keys.extend([x for x in array.keys() if not isinstance(basestring, x)])
    return keys
