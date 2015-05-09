import binascii

import os


def make_guid():
    return binascii.b2a_hex(os.urandom(64))
