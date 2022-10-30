def alg(n):
    r = bin(n)[2:]
    r = r + str(sum(map(int, r)) % 2)
    r = r + str(sum(map(int, r)) % 2)
    return int(r, 2)


for i in range(1, 28):
    if alg(i) > 77:
        print(i)
        break