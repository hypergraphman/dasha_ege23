for i in range(10000, 0, -1):
    s = i
    n = 8
    while n < 510:
        s = s + (n // 2)
        n = 2 + n
    if s == 32299 + 510:
        print(i)
        break
