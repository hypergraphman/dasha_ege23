for x in range(94):
    for y in range(63):
        for z in range(32):
            if 2 * x + 3 * y + 6 * z == 186 and \
               y + z == 26:
                print(x, y, z, x + y + z + 2)