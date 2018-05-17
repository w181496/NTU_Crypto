from pwn import *

BS = 16 # block size

A = '296e12d608ad04bd3a10b71b9eef4bb6ae1d697d1495595a5f5b98e409d7a7c437f24e69feb250b347db0877a40085a9'
B = '296e12d608ad04bd3a10b71b9eef4bb6ae1d697d1495595a5f5b98e409d7a7c437f24e69feb250b347db0877a40085a9'

P1 = ''
P2 = ''

r = remote('140.112.31.96', 10124)
r.recvuntil('> ')
r.sendline('1')
r.recvuntil('Ciphertext: ')
r.sendline(A)
P1 = r.recvline()[:-1] # Decrypt(A1||A2||A3)
print("P1 len:", len(P1))
print(P1.encode('hex'))

r = remote('140.112.31.96', 10124)
r.recvuntil('> ')
r.sendline('1')
r.recvuntil('Ciphertext: ')
r.sendline(B+A)
P2 = r.recvline()[:-1] # Decrypt(A1||A2||A3||A1||A2||A3)
print("P2 len:",len(P2))
print(P2.encode('hex'))

tmp = A.decode('hex')[32:]  # A3
s1 = P2[48:][:16] # (A3 xor D(A1))
DA = ''
for i in range(len(s1)):
    DA += chr(ord(s1[i]) ^ ord(tmp[i]))
print("D(A1):",DA)

ans = ''
tmp = P2[:16]
for i in range(len(DA)):
    ans += chr(ord(DA[i]) ^ ord(tmp[i]))
print("IV:",ans)

#r.interactive()
