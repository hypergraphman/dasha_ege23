for a in range(1, 100):
    is_a = True
    for k in range(1, 100):
        for n in range(1, 100):
            f = (5 * k + 6 * n > 57) or ((k <= a) and (n < a))
            if not f:
                is_a = False
                break
    if is_a:
        print(a)