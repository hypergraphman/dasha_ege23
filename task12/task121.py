line = '5' * 146
while '333' in line or '555' in line:
    if '555' in line:
        line = line.replace('555', '3', 1)
    else:
        line = line.replace('333', '5', 1)
print(line)