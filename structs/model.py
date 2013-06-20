from collections import OrderedDict
from structs.exceptions import InvalidData
from structs.fields import BaseStructField

__all__ = ('StructModel',)


class StructMeta(type):
    def __new__(cls, model, bases, attrs):
        new_cls = type.__new__(cls, model, bases, attrs)
        declared_fields = [(key, value) for key, value in attrs.iteritems() if isinstance(value, BaseStructField)]
        new_cls._fields = OrderedDict(sorted(declared_fields, key=lambda x: x[1]._creation_counter))
        return new_cls


class StructModel(object):
    """
    Class used to define a model
    """
    __metaclass__ = StructMeta

    def __init__(self, data):
        self._struct = ''.join(field.struct_type for field in self._fields.itervalues())
        if isinstance(data, basestring):
            pass
        else:
            raise InvalidData('Only string is supported for now.')
