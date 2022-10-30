import itertools


def avt(n):
    a = list(str(n))
    t = []
    for pair in itertools.permutations(a, 2):
        num = int(''.join(pair))
        if 10 <= num <= 99:
            t.append(num)
    return max(t) - min(t)


for i in range(100, 1000):
    if avt(i) == 40:
        print(i)
