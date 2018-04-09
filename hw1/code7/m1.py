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

    def encrypt0(self, s):
        return self.aes128_0.encrypt(s)
    
    def encrypt1(self, s):
        return self.aes128_1.encrypt(s)

    def decrypt(self, data):
        return self.aes128_0.decrypt(self.aes128_1.decrypt(data))
    
    def decrypt0(self, data):
        return self.aes128_0.decrypt(data)
    
    def decrypt1(self, data):
        return self.aes128_1.decrypt(data)

def int2bytes(n):
    return bytes.fromhex('{0:032x}'.format(n))

key = 0

for i in range(2 ** 23):
    key = i

    aes2 = DoubleAES(key0=int2bytes(key), key1=int2bytes(key))

    p1 = 'NoOneUses2AES_QQ'
    c1 = '0e46d393fdfae760f9d4c7837f47ce51'

    m1 = aes2.encrypt0(p1).hex()
    print(m1, key)

