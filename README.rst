Structs (Python Struct for Humans)
==================================

structs is intended to make life easier when you have to speak with binary data on python

The idea is something like this:

Instead of (magic, opcode, key_length, ext_length, data_type, status, body_length, opaque, cas) = struct.unpack('!BBHBBHLLQ', value) you would do this:


.. code-block:: python

    from structs.model import StructModel
    from structs import fields

    class MemcachedProtocol(StructModel):
        magic = fields.UChar()
        opcode = fields.UChar()
        key_length = fields.UShort()
        ext_length = fields.UChar()
        data_type = fields.UChar()
        status = fields.UShort()
        body_length = fields.ULong()
        opaque = fields.ULong()
        cas = fields.ULongLong()

    protocol_return = MemcachedProtocol(data)

    # Now access unpacked binary data with:
    assert protocol_return.magic == 129  # 0x81 to integer


