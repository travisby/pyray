"""Utilities for our python PHP array"""
import collections


class PyRay:
    """PHP Array in Python"""

    _obj = collections.OrderedDict()

    def __init__(self):
        """Sets our data members to their default state"""
        self._obj = collections.OrderedDict()

    def __repr__(self):
        header = 'PyRay(%(len)s) {' % {'len': len(self)}
        body = ''.join([self._repr_body(item) for item in self._obj.items()])
        return '%s %s \n }' % (header, body)


    def _repr_body(self, item):
        return (
            '\n\t["%(key)s"]=>\n\t%(type)s %(val)s' %
            {'key': item[0], 'type': type(item[1]), 'val': item[1]}
        )

    def __len__(self):
        """What we interpret our size to be"""
        return len(self._obj.keys())
