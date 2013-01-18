"""Utilities for our python PHP array"""
import collections


class UndefinedIndex(KeyError):
    """Raised when a requested index does not exist"""
    pass


class PyRay:
    """PHP Array in Python"""

    _obj = collections.OrderedDict()

    def keys(self):
        """Returns a list of our keys"""
        return self._obj.keys()

    def _get_int_keys(self):
        """Return a list of the integer keys"""
        return [x for x in self._obj.keys() if isinstance(x, int)]

    def _get_largest_int_key(self):
        """Return the largest of our integer keys"""
        keys = self._get_int_keys()
        keys.sort()
        return keys[-1]

    def _get_next_largest_int_key(self):
        """Return the next numerical index"""
        return self._get_largest_int_key + 1

    def __init__(self):
        """Sets our data members to their default state"""
        self._obj = collections.OrderedDict()

    def __repr__(self):
        """Used for a string representation"""
        header = 'PyRay(%(len)s) {' % {'len': len(self)}
        body = ''.join([self._repr_body(item) for item in self._obj.items()])
        return '%s %s \n }' % (header, body)

    @staticmethod
    def _repr_body(item):
        """Partial for __repr__"""
        return (
            '\n\t["%(key)s"]=>\n\t%(type)s %(val)s' %
            {'key': item[0], 'type': type(item[1]), 'val': item[1]}
        )

    def __len__(self):
        """What we interpret our size to be"""
        return len(self._obj.keys())

    def __getitem__(self, key):
        """Attempts to access based on the provided index"""
        try:
            return self._obj[key]
        except KeyError:
            raise UndefinedIndex

    def __setitem__(self, key, value):
        """Sets key => value
        except when key = '', which grabs the next largest numeral
        will convert strings to numbers  wherever possible
        """
        if key:
            # PHP will convert strings to number keys if possible
            # int() will convert to long if the key is too large
            try:
                key = int(key)
            except ValueError:
                # guess we can't convert it :P
                pass
            self._obj[key] = value
        else:
            self._obj[self._get_next_largest_int_key()] = value

    def __delitem__(self, key):
        """Delets a key"""
        del(self._obj[key])

    def __iter__(self):
        """Returns an iterator over our values"""
        return self._obj.itervalues()

    def __contains__(self, item):
        """Returns whether or not an element exists in our array"""
        # Note that php's in_array() checks values, not keys like python
        # usually does
        return item in self._obj.values()
