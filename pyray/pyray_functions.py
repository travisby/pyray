"""Methods that can be used on pyrays"""
import pyray

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

