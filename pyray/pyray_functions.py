"""Methods that can be used on pyrays"""
import pyray

def array_keys(array, search_value=None):
    if not search_value:
        return array.keys()

