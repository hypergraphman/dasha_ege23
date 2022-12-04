def f(line):
    while '111' in line or '333' in line:
        if '111' in line:
            line = line.replace('111', '3', 1)
        else:
            line = line.replace('333', '1', 1)
    return line


for i in range(101, 120):
    print(i, f('3' * i))
