f = open('17-338.txt')
a = []
for el in f:
    a.append(int(el))

mn = 2**64
for el in a:
    if el < mn:
        mn = el

c = 0
mx_s = 0
for i in range(1, len(a)):
    e1, e2 = a[i - 1], a[i]
    if e1 % 117 == mn or e2 % 117 == mn:
        c += 1
        if e1 + e2 > mx_s:
            mx_s = e1 + e2
print(c, mx_s)
