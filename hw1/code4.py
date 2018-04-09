from pwn import *
import sys
import itertools

#r = remote('127.0.0.1', 10120)
r = remote('140.112.31.96', 10120)


flag = ''
ans = ''

# round 0 
print "====== round 0 ======"
r.recvuntil("m1 = ")
m1 = r.recvline()[:-1]

r.sendline(m1)

# round 1
print "====== round 1 ======"
r.recvuntil("c1 = ")
c1 = r.recvline()[:-1]
tmp = c1.split(' ')
for i in range(len(tmp)):
    for j in range(len(tmp[i]) / 2):
        ans += chr(int(tmp[i][2 * j] + tmp[i][2 * j + 1]) - 1 + ord('a')) 
    ans += ' '

r.sendline(ans.strip())
r.recvuntil("FLAG_PIECES: ")
flag += r.recvline()[:-1]


# round 2
print "====== round 2 ======"
r.recvuntil("m1 = ")
m1 = r.recvline()[:-1]
r.recvuntil("c1 = ")
c1 = r.recvline()[:-1]

diff = ord(c1[0]) - ord(m1[0])

if diff < 0:
    diff += 26

r.recvuntil("c2 = ")
c2 = r.recvline()[:-1]

ans = ''

for i in range(len(c2)):
    if c2[i] != ' ':
        asc = ord(c2[i]) - diff
        if ord(c2[i]) >= ord('a'):
            if asc > ord('z'):
                asc -= 26
            elif asc < ord('a'):
                asc += 26
        else:
            if asc > ord('Z'):
                asc -= 26
            elif asc < ord('A'):
                asc += 26
            
        ans += chr(asc)
    else:
        ans += ' '


r.sendline(ans.strip())

r.recvuntil("FLAG_PIECES: ")
flag += r.recvline()[:-1]


# round 3
print "====== round 3 ======"
choice = []
r.recvuntil("c1 = ")
c1 = r.recvline()[:-1]
for i in range(25):
    tmp = ''
    for j in range(len(c1)):
        asc = ord(c1[j]) + i
        if c1[j] == ' ':
            asc = 32
        elif c1[j] >= ord('a'):
            if asc > ord('z'):
                asc -= 26
        else:
            if asc > ord('Z'):
                asc -= 26
        tmp += chr(asc)
    choice.append(tmp)

check = 0
word = ["physics", "cryptography", "electronic", "Application", "application", "military", "thereby", "persons", "adversary", "development", "effectively", "readable", "authentication", "confidentiality", "adversaries", "public", "decoding", "computer", "digital", "odern", "communication", "message", "information", "technique", "become", "protocols"]
ans = ''
for i in range(len(choice)):
    for j in word:
        if j in choice[i]:
            check = 1
            ans = choice[i]
            print "found!"
            break
    print i, ":", choice[i]

if check == 1:
    r.sendline(ans)
else:
    ans = sys.stdin.readline()
    r.sendline(choice[int(ans[:-1])])
#ans = raw_input("input choice:")
#r.sendline(ans[:-1])

r.recvuntil("FLAG_PIECES: ")
flag += r.recvline()[:-1]


# round 4
print "====== round 4 ======"
r.recvuntil("m1 = ")
m1 = r.recvline()[:-1]
r.recvuntil("c1 = ")
c1 = r.recvline()[:-1]

print "m1:",m1
print "c1:",c1

d = {}
for i in range(len(m1)):
    d[c1[i]] = m1[i]

r.recvuntil("c2 = ")
c2 = r.recvline()[:-1]

ans = ''
for i in range(len(c2)):
    if c2[i] in d.keys():
        ans += d[c2[i]]
    else:
        ans += '_'


print ans
print c2


ans = sys.stdin.readline()
r.sendline(ans[:-1])

r.recvuntil("FLAG_PIECES: ")
flag += r.recvline()[:-1]


# round 5 transposition cipher
print "====== round 5 ======"
r.recvuntil("m1 = ")
m1 = r.recvline()[:-1]
r.recvuntil("c1 = ")
c1 = r.recvline()[:-1]

print "m1:", m1
print "c1:", c1

r.recvuntil("c2 = ")
c2 = r.recvline()[:-1]

print "c2:", c2


lengths = []
temp = 0
segment = c1[1]
while (temp < len(c1)):
    i = m1.find(segment, temp)
    if i == -1: break
    else:
        temp = i+1
        lengths.append(i)
print(lengths)
for length in lengths:
    size = len(m1) // length
    rest = len(m1) % length
    m1_segment = []
    c1_segment = c1[0:size + 1]
    for i in range(size):
        m1_segment.append(m1[i * length: (i + 1) * length]) 
    if rest != 0: 
        m1_segment.append(m1[size * length:])
        size += 1
    verif = ''
    for i in range(size):
        verif += m1_segment[i][0]
    if c1_segment != verif:
        continue
    print(m1_segment, length, c1_segment)
    counter = 0
    key = [0]
    ci = size
    for i in range(length):
        counter += 1
        mi = 1
        tag = True
        while mi < length:
            if len(key) == length: break
            mi = m1_segment[0].find(c1[ci], mi)
            if mi == -1: break
            elif mi in key:
                mi+=1
                continue
            verif = ''
            for j in range(size):
                if mi < len(m1_segment[j]):
                    verif += m1_segment[j][mi]
            if verif == c1[ci:ci+len(verif)]:
                ci += len(verif)
                key.append(mi)
                tag = False
                break
            else: mi += 1
        if (tag): break
    if (len(key) == length): break
print(key)
print(length)
c2_segment = [''] * length
size = len(c2) // length
rest = len(c2) %  length
index = 0
for i in key:
    if i < rest:
        c2_segment[i] = c2[index: index + (size + 1)]
        index += (size + 1)
    else:
        c2_segment[i] = c2[index: index + size]
        index += size
result = ''
if result != 0: 
    size += 1
for i in range(size):
    for sg in c2_segment:
        if i < len(sg):
            result += sg[i]

r.sendline(result)
r.recvuntil("FLAG_PIECES: ")
flag += r.recvline()[:-1]
print "flag:",flag

# round 6
print "====== round 6 ======"
r.recvuntil("m1 = ")
m1 = r.recvline()[:-1]
r.recvuntil("c1 = ")
c1 = r.recvline()[:-1]

print "m1:", m1
print "c1:", c1

gap = m1.find(c1[1])

r.recvuntil("c2 = ")
c2 = r.recvline()[:-1]

print "c2:", c2

segment = len(c2) / gap
if len(c2) % gap > 0 :
    segment += 1
ans = ['_'] * len(c2) + ['#'] * (gap - len(c2) % gap)

now = 0

for i in range(segment):
    ans[i * gap] = c2[i]


l = [gap - 1] * segment
k = []

for i in range((segment)):
    k.append([1, gap - 1])

for i in range((len(c2) - segment) / 2 + 100):
    if l[now] <= 0:
        now = (now + 1) % segment
    if segment + 2 * i + 1 >= len(c2):
        break
    print "now:", now
    print "k[now][0]:",k[now][0]
    print "k:",k
    print now * gap + k[now][0]
    print 'ans:',''.join(ans)
    ans[now * gap + k[now][0]] = c2[segment + 2 * i]
    if k[now][0] != k[now][1]:
        if ans[now * gap + k[now][1]] == '#':
            c2 = c2[:segment + 2 * i + 2] + c2[segment + 2 * i + 1:]
        else:
            ans[now * gap + k[now][1]] = c2[segment + 2 * i + 1]
    else:
        c2 = c2[:segment + 2 * i + 2] + c2[segment + 2 * i + 1:]
    k[now][0] += 1
    k[now][1] -= 1
    l[now] -= 2
    now = (now + 1) % segment

print ''.join(ans)


r.interactive()
