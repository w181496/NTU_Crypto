from pwn import *
from hashlib import sha1
import gmpy2

#r = remote('localhost', 10123)
r = remote('140.112.31.96', 10123)

token = 'hN3evxpaBjT8cWIFMF6T48C5gIglCF8uSndIA5HCr3nM3OF5TAioHwfUSmzFNMvmeRGVX2i+ygmgDHqolpNit2cocDS/8g0MOb2KR69EgVI='
user = 'aaaaaaaaaa'
pwd = 'bbbbbbbbbbbbbbbbbbbbb'

# login by copy and paste attack
r.sendline('1') 
r.sendline(token)
r.sendline(user)
r.sendline(pwd)

# transaction
r.sendline('0')

r.recvuntil('Transaction1: ')
t1 = r.recvline()[:-1]
print "t1:",t1

r.recvuntil(': ')
r1, s1, shit = r.recvline().split(' ')
print "r1:",r1
print "s1:",s1

r.recvuntil('Transaction2: ')
t2 = r.recvline()[:-1]
print "t2:",t2

r.recvuntil(': ')
r2, s2, shit  = r.recvline().split(' ')
print "r2:",r2
print "s2:",s2

print

# public key
r.sendline('1')

r.recvuntil('p = ')
p = r.recvline()[:-1]
print "p:",p

r.recvuntil('q = ')
q = r.recvline()[:-1]
print "q:",q

r.recvuntil('g = ')
g = r.recvline()[:-1]
print "g:",g

r.recvuntil('y = ')
y = r.recvline()[:-1]
print "y:",y

# start cracking private key
sha = sha1()
sha.update(t1)
m1 = int(sha.hexdigest(), 16)

sha = sha1()
sha.update(t2)
m2 = int(sha.hexdigest(), 16)

ds = int(s2) - int(s1)
dm = m2 - m1
k = gmpy2.mul(dm, gmpy2.invert(ds, int(q)))
k = gmpy2.f_mod(k, int(q))
tmp = gmpy2.mul(k, int(s1)) - m1
x = tmp * gmpy2.invert(int(r1), int(q))
x = gmpy2.f_mod(x, int(q))
print "x:",x

# sign "FLAG"
k = 1
r3 = ((int(g) ** k) % int(p)) % int(q)
sha = sha1()
sha.update('FLAG')
m3 = int(sha.hexdigest(), 16)
s3 = (m3 + x * r3) % int(q)

print "r:", r3
print "s:", s3

r.sendline(r3)
r.sendline(s3)

r.interactive()

