class BaseStructField(object):
    pass


class Char(BaseStructField):
    """string of length 1"""
    struct_type = 'c'


class UChar(BaseStructField):
    """unsigned integer of size 1"""
    struct_type = 'B'


class SChar(BaseStructField):
    """signed integer of size 1"""
    struct_type = 'b'


class Short(BaseStructField):
    """signed integer of size 2"""
    struct_type = 'h'


class UShort(BaseStructField):
    """unsigned integer of size 2"""
    struct_type = 'H'


class Int(BaseStructField):
    """signed integer of size 4"""
    struct_type = 'i'


class UInt(BaseStructField):
    """unsigned integer of size 4"""
    struct_type = 'I'


class Long(BaseStructField):
    """signed integer of size 4"""
    struct_type = 'l'


class ULong(BaseStructField):
    """unsigned integer of size 4"""
    struct_type = 'L'


class LongLong(BaseStructField):
    """signed integer of size 8"""
    struct_type = 'q'


class ULongLong(BaseStructField):
    """unsigned integer of size 8"""
    struct_type = 'Q'


class Float(BaseStructField):
    """float of size 4"""
    struct_type = 'f'


class Double(BaseStructField):
    """float of size 8"""
    struct_type = 'd'


class String(BaseStructField):
    """string"""
    struct_type = 's'
