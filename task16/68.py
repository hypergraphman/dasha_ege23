def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return f(n - 2) + n - 2
    if n >= 3 and n % 2 == 1:
        return f(n + 2) + n + 2


c = 0
for i in range(1, 20000):
    try:
        if len(str(f(i))) == 5:
            c += 1
    except:
        pass
print(c)
