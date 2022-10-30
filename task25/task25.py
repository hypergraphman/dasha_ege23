from math import sqrt


def f(n):
    dels = {1, n}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)


# max_ns = [[1, 1]]
# for i in range(586132, 586430 + 1):
#     i_dels = len(f(i))
#     if max_ns[0][1] < i_dels:
#         max_ns = [[i, i_dels]]
#     elif max_ns[0][1] == i_dels:
#         max_ns.append([i, i_dels])
# print(*max_ns, sep='\n')

print(80, 585224, 293112)
print(80, 586320, 293160)