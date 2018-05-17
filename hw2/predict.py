a = raw_input(":")
b = raw_input(":")
c = raw_input(":")
d = raw_input(":")
e = raw_input(":")

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

ans = ''

ans += hex(a)[2:]
ans += hex(b)[2:]
ans += hex(c)[2:]
ans += hex(d)[2:]
ans += hex(e)[2:]

print ans
