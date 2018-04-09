import base64
import hashpumpy
from pwn import *
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def sha256(content):
    Sha256 = SHA256.new()
    Sha256.update(content)
    return Sha256.digest()

r = remote('localhost', 10122)
r2 = remote('localhost', 10122)

r.recvuntil('You should send your ID and a random string to me:')
r2.recvuntil('You should send your ID and a random string to me:')

ID = 'admin'
Nc = 'admin'

r.sendline(ID + '||' + Nc + '||' + base64.b64encode(sha256(ID + '||' + Nc)))

d = r.recvline()
Ns =  d.split('||')[0][1:]
h = base64.b64decode(d.split('||')[1]).encode('hex')
print "Ns:",Ns
print "h:",h

r2.sendline(ID + '||' + Ns + '||' + base64.b64encode(sha256(ID + '||' + Ns)))

d = r2.recvline()
print "d:",d

h2 = base64.b64decode(d.split('||')[1]).encode('hex')
print "h2:",h2

orig = ID + '||' + Ns + '||login'

res = hashpumpy.hashpump(h2, orig, '||printflag', 21)
mac, message = res
print mac
print message

payload = base64.b64encode(message) + '||' + base64.b64encode(mac.decode('hex'))

print "payload:",payload
r.sendline(payload)
r.interactive()
