for x in range(57):
    for y in range(57):
        for z in range(57):
            if x + 2 * y + 3 * z == 56 and x + y + 3 * z == 44 and y + z == 19:
                print(x + y + z + 2)