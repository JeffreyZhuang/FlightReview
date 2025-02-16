import struct
from cobs import cobs

struct_format = 'II3f'

file = open('log118.bin', 'rb')

while True: 
    byte = file.read(1)

    # Find start byte
    if byte == b'\x00':
        packet_cobs = file.read(struct.calcsize(struct_format) + 1) # Add 1 because COBS byte
        packet = cobs.decode(packet_cobs)
        data = struct.unpack(struct_format, packet)
        print(data)