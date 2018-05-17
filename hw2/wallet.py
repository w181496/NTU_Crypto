from pwn import *

r = remote('140.112.31.96', 10128)

adr = []
pwd = []
state = []
tmp = []

def get_adr_pwd():
    # address
    r.recvuntil('Address: ')
    tmp = r.recvline()[:-1]
    for i in range(3):
        s = tmp[8 * i:][:8]
        s = int(s, 16)
        adr.append(s)
        state.append(s)

    # password
    r.recvuntil('Password: ')
    tmp = r.recvline()[:-1]
    for i in range(5):
        s = tmp[8 * i:][:8]
        s = int(s, 16)
        pwd.append(s)
        state.append(s)

for i in range(100):
    get_adr_pwd()

with open('state', 'w+') as f:
    for i in range(len(state)):
        f.write(str(state[i])+"\n")

r.recvuntil('Address: ')
tmp = r.recvline()[:-1]
for i in range(3):
    s = tmp[8 * i:][:8]
    s = int(s, 16)
    print s

r.interactive()  # 會停在這，開另一個terminal算password
