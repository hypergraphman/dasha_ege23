from math import sqrt


def len_dels(n):
    dels = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return len(dels)


def mult(nums):
    res = 1
    for n in nums:
        res *= n
    return res


primes = []
i = 2
while mult(primes) < 10_000_000:
    if len_dels(i) == 0:
        primes.append(i)
    i += 1
print(mult(primes[:-1]), len(primes[:-1]))