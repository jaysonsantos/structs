from collections import OrderedDict
import struct
from structs.exceptions import InvalidData, InvalidDataSize
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
        size = struct.calcsize(self._struct)
        if len(data) != size:
            raise InvalidDataSize('Data is expected to have %d bytes and it have %d bytes' % (size, len(data)))

        if isinstance(data, basestring):
            data = struct.unpack(self._struct, data)
            for i, field in enumerate(self._fields.itervalues()):
                if i == 0:
                    continue

                field.value = data[i - 1]

        else:
            raise InvalidData('Only string is supported for now.')
