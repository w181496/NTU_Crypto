from pwn import *
import hashlib

r = remote('localhost', 10121)

r.recvuntil("=??????????????????????????????????")
d = r.recvuntil(":")[:-1]
print d

r1 = ""
r2 = ""
with open("shattered-1.pdf") as f:
    r1 = f.read().strip()[:320]
    print hashlib.sha1(r1[:320]).hexdigest()

with open("shattered-2.pdf") as f:
    r2 = f.read().strip()[:320]
    print hashlib.sha1(r2[:320]).hexdigest()

nonce = 0
while True:
    if nonce % 1000 == 0:
        print nonce, hashlib.sha1(r1 + str(nonce)).hexdigest()[-6:]
    if hashlib.sha1(r1 + str(nonce)).hexdigest()[-6:] == d :
        print "found!", nonce
        x = r1 + str(nonce)
        y = r2 + str(nonce)
        r.sendline(x.encode('hex'))
        r.sendline(y.encode('hex'))
        break
    nonce += 1

r.interactive()
