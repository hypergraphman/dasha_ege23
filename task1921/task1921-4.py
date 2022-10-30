from math import ceil

N1, WIN = 5, 53
KADD, KMUL = 1, 2

results = dict()


def game_result(x, y):
    # Если пара-ключ х и у присутствует в словаре результат, то мы возвращаем число по этой паре-ключ
    if (x, y) in results:
        return results[(x, y)]
    # условие окончания игры
    if x + y >= WIN:
        return 0
    next_codes = [
        game_result(x + KADD, y),
        game_result(x * KMUL, y),
        game_result(x, y + KADD),
        game_result(x, y * KMUL)
    ]
    negative = [c for c in next_codes if c <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(next_codes)
    results[(x, y)] = res
    return res


ans1 = min(ceil((WIN - N1) / KMUL / KMUL), WIN - N1 * KMUL * KMUL)
ans2 = []
ans3 = []
for S in range(WIN - N1 - 1, 0, -1):
    r = game_result(N1, S)
    print("%d: %d" % (S, r))
    if r == 2:
        ans2.append(S)
    if r == -2:
        ans3.append(S)

# -------------------------------------------------------
# Ответы на вопросы
# -------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", ans3)
