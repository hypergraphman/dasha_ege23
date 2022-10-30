s = open('10-0.txt').readlines()
for line in s:
    if 'портрет' in line or 'Портрет' in line:
        print(line.strip())