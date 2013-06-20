from structs import model
from structs import fields


class MemcachedProtocol(model.StructModel):
    byte_order = fields.NetworkByteOrder()
    magic = fields.UChar()
    opcode = fields.UChar()
    key_length = fields.UShort()
    ext_length = fields.UChar()
    data_type = fields.UChar()
    status = fields.UShort()
    body_length = fields.ULong()
    opaque = fields.ULong()
    cas = fields.ULongLong()


def test_unpacking():
    p = MemcachedProtocol('0x81')
    import ipdb;ipdb.set_trace()
    assert p.magic == 129