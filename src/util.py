import os

def true_pyrand():
    return int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
