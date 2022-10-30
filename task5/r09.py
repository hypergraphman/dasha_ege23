def alg(n):
    # a1, a2, a3, a4 = map(int, str(n))
    a1 = n // 1000
    a2 = n // 100 % 10
    a3 = n // 10 % 10
    a4 = n % 10
    a = []
    a.append(a1 + a2)
    a.append(a3 + a2)
    a.append(a3 + a4)
    a.sort()
    return str(a[1]) + str(a[2])


for i in range(1000, 10000):
    if alg(i) == '511':
        print(i)