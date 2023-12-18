

import hashlib

def generate_ji(i, X, Y, k1, k2):
    v = i // X
    u = i % X
    ji = v * X + u
    for _ in range(10):
        v = (v + int(hashlib.md5(str(u + k1).encode()).hexdigest(), 16)) % Y
        u = (u + int(hashlib.md5(str(v + k2).encode()).hexdigest(), 16)) % X
        ji = v * X + u
    return ji

# Example usage
block_size = 4
X = Y = 512 // block_size
total_carrier_units = X * Y
indexes_of_blocks_for_watermark_embedding = [generate_ji(i, X, Y, 123, 456) for i in range(total_carrier_units)]
