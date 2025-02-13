import struct

struct_format = 'Q2f'

file = open('log1.bin', 'rb')

while True: 
    data = file.read(struct.calcsize(struct_format))
    unpacked_data = struct.unpack(struct_format, data)
    print(unpacked_data)