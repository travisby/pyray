"""Utilities for our python PHP array"""
import collections


class PyRay:
    """PHP Array in Python"""

    _obj = collections.OrderedDict()

    def __init__(self):
        """Sets our data members to their default state"""
        self._obj = collections.OrderedDict()
