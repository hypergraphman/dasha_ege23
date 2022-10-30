for i in range(223334511, 223456000):
# x = 223334511
    x = i
    n = 1234
    while (x + n) // 1000 < 223456:
        x = x - 2
        n = n + 3
    print(n // 1000)
    if n // 1000 == 361:
        print(i)