m1 = ''
m2 = ''
with open('m1-sorted') as f1:
    m1 = f1.read()

with open('m2-sorted') as f2:
    m2 = f2.read()


a = m1.split("\n")
b = m2.split("\n")

len1 = len(a)
len2 = len(b)

pa = 0
pb = 0
i = 0
ans = []
while(pa < len1 and pb < len2):
    ca = a[pa].split(' ')[0]
    cb = b[pb].split(' ')[0]
    if ca == cb:
        print "found!", a[pa]
        ans.append(a[pa] + ' ' + b[pb])
        pa += 1
        pb += 1
        #break
    else:
        if ca > cb :
            pb += 1
        else:
            pa += 1
    i += 1

for i in ans:
    print i
