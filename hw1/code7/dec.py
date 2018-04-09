#!/usr/bin/env python3
# Python 3.6.4

from Crypto.Cipher import AES
import codecs

flag = '????????????????????????????????'
assert len(flag) == 32

class DoubleAES():
    def __init__(self, key0, key1):
        self.aes128_0 = AES.new(key=key0, mode=AES.MODE_ECB)
        self.aes128_1 = AES.new(key=key1, mode=AES.MODE_ECB)

    def encrypt(self, s):
        return self.aes128_1.encrypt(self.aes128_0.encrypt(s))

    def decrypt(self, data):
        return self.aes128_0.decrypt(self.aes128_1.decrypt(data))

def int2bytes(n):
    return bytes.fromhex('{0:032x}'.format(n))

key = 1111111111
assert key < 2**46
key0, key1 = key // (2**23), key % (2**23)
assert key0 < 2**23 and key1 < 2**23

key0 = 6298659
key1 = 4272711

aes2 = DoubleAES(key0=int2bytes(key0), key1=int2bytes(key1))

flag_enc = '3e3a9839eb6331aa03f76e1a908d746bfccaf7acb22265b725a9f1fc0644cdda'
flag = aes2.decrypt(codecs.decode(flag_enc, 'hex_codec'))
print(flag)
