# this script is to solve "First" block
# if you want to solve other block, just modify the IV and payload
from pwn import *

A = 'a' * 15
flag_enc = '6cda1158b540cb0f69bf1aff4260916f7622e2203f7458d69d0525f50c0061499ae4048b2b5a6b4e8928a30bb00595fba2ea649970567930e436c877e9de7056f5ac97b4baf4aedc53f441fa50c7d25f'
flag_enc_dec = flag_enc.decode('hex')
IV = flag_enc_dec[:16]
ok = ''
rec = ''
flag = ''
for j in range(16):
    A = 'g' * (16 - j - 1)
    for i in range(256):
        r = remote('140.112.31.96', 10125)
        r.recvuntil('> ')
        r.sendline("1")
        r.recvuntil('How2decrypt? QQ')
        r.recvline()
        r.recvline()
        tmp = A + chr(i) + ok
        payload = tmp.encode('hex') + flag_enc_dec[16:][:16].encode('hex')
        print "payload",payload
        r.sendline(payload)
        res = r.recvline()
        if 'Success' in res:
            print "Found!",i
            tmp = i ^ (j + 1)
            ans = ord(IV[-1 * (j + 1)]) ^ tmp
            print chr(ans)
            flag = chr(ans) + flag
            print flag
            rec = chr(tmp) + rec
            ok = ''
            for k in range(len(rec)):
                ok += chr(ord(rec[k]) ^ (j + 2))
            print "ok:",ok.encode('hex')
            break
        r.close()
