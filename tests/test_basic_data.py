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
    p = MemcachedProtocol('\x81\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c')
    assert p.magic == 129
    p.magic = 123