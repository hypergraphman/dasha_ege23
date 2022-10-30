# s1, s2 = heap_1, heap_2
win = 75
add, mul = 1, 2
for k in range(win - 7 - 1, 15, -1):
    heap_1, heap_2 = 7, k
    history = {0: {(heap_1, heap_2, heap_1 + heap_2)}}
    for i in range(1, win):
        history[i] = set()
    for i in range(win - 1):
        for turn in history[i]:
            s1, s2, s = turn
            if s < win:
                history[i + 1].add((s1 + add, s2, s1 + add + s2))
                history[i + 1].add((s1, s2 + add, s1 + s2 + add))
                history[i + 1].add((s1 * mul, s2, s1 * mul + s2))
                history[i + 1].add((s1, s2 * mul, s1 + s2 * mul))

    for turn in history[4]:
        if turn[2] >= win:
            print(k, turn)