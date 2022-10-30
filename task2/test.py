for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            print(a, b, c, int(not (a and b) or not(b and (not c))))