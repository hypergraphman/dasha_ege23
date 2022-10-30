from math import sqrt


def sum_dels(n):
    dels = {1}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sum(dels)


for i in range(2, 30000):
    num = sum_dels(i)
    if i == sum_dels(num) and num > i:
        print(i, num)
