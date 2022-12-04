def n_to_p(n, p):
    res = ''
    while n > 0:
        res = '0123456789ABCDEF'[n % p] + res
        n //= p
    return res


x = 3**37 + 2*3**23 + 3*3**20 + 4 * 3**4 + 5 * 3 ** 3 + 4 + 5
p = 9
print(n_to_p(x, p).count('0'))

x = 3**72 + 6 * 3**50 - 7 * 3**26 + 2 * 3**15 + 155
p = 9
print(len(set(n_to_p(x, p))))
