import binascii

import os


def make_guid(length=32):
    return binascii.b2a_hex(os.urandom(length))
