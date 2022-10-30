def avt(n):
    n2 = bin(n)[2:]
    x2 = n2[1:]
    x = int(x2, 2)
    return n - x


s = set()
for i in range(500, 5000 + 1):
    s.add(avt(i))
print(len(s))