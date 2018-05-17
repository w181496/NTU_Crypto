import hashlib
from pwn import *

p = 262603487816194488181258352326988232210376591996146252542919605878805005469693782312718749915099841408908446760404481236646436295067318626356598442952156854984209550714670817589388406059285064542905718710475775121565983586780136825600264380868770029680925618588391997934473191054590812256197806034618157751903

def s(r, r2):
    r.recvuntil('Server sends: ')
    a = r.recvline()[:-1]
    r.recvuntil(': ')
    r2.recvuntil('Server sends: ')
    b = r2.recvline()[:-1]
    r2.recvuntil(': ')
    r.sendline(b)
    r2.sendline(a)

def f(r, r2, pwd):
    r.recvuntil('Server sends: ')
    a1 = r.recvline()[:-1]
    r.recvuntil(': ')
    r.sendline(str(pwd))
    r2.recvuntil('Server sends: ')
    b1 = r2.recvline()[:-1]
    r2.recvuntil(': ')
    r2.sendline(str(pwd))
    return a1, b1

def crack_pwd():
    for j in range(3):
        for i in range(20):
            r = remote('140.112.31.96', 10127)
            r2 = remote('140.112.31.96', 10127)

            pwd = pow(int(hashlib.sha512(str(i+1)).hexdigest(), 16), 2, p)

            for q in range(j):
                s(r, r2)

            a1, b1 = f(r, r2, pwd)

            for q in range(3 - j - 1):
                s(r, r2)

            r.recvuntil('FLAG is: ')
            r2.recvuntil('FLAG is: ')
            FLAG1 = int(r.recvline()[:-1])
            FLAG2 = int(r2.recvline()[:-1])

            k1 = int(hashlib.sha512(a1).hexdigest(), 16)
            k2 = int(hashlib.sha512(b1).hexdigest(), 16)

            if (FLAG1 ^ k1) == (FLAG2 ^ k2):
                print j + 1, ":", i + 1
                break

crack_pwd()
pwd1 = 13
pwd2 = 19
pwd3 = 17

g1 = pow(int(hashlib.sha512(str(pwd1)).hexdigest(), 16), 2, p)
g2 = pow(int(hashlib.sha512(str(pwd2)).hexdigest(), 16), 2, p)
g3 = pow(int(hashlib.sha512(str(pwd3)).hexdigest(), 16), 2, p)

r = remote('140.112.31.96', 10127)

key = 0

r.recvuntil('Server sends: ')
a = r.recvline()[:-1]
r.recvuntil(': ')
r.sendline(str(g1))

K = int(a)
key ^= int(hashlib.sha512(str(K)).hexdigest(), 16)

r.recvuntil('Server sends: ')
a = r.recvline()[:-1]
r.recvuntil(': ')
r.sendline(str(g2))
K = int(a)
key ^= int(hashlib.sha512(str(K)).hexdigest(), 16)

r.recvuntil('Server sends: ')
a = r.recvline()[:-1]
r.recvuntil(': ')
r.sendline(str(g3))
K = int(a)
key ^= int(hashlib.sha512(str(K)).hexdigest(), 16)

r.recvuntil('FLAG is: ')
FLAG = int(r.recvline()[:-1])

FLAG ^= key

print FLAG
print hex(FLAG)[2:].decode('hex')
