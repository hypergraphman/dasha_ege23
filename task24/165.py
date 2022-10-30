from itertools import product

def f1(n):
    return n + 1
def f2(n):
    return n + 3
def f3(n):
    return n * 2

n_cmd = ['1', '2', '3']
pgrms = product(n_cmd, repeat=13)
set_pgrms = set()
for cmds in pgrms:
    n = 1
    c = 0
    for cmd in cmds:
        c += 1
        if cmd == '1':
            n = f1(n)
        if cmd == '2':
            n = f2(n)
        if cmd == '3':
            n = f3(n)
        if n == 14:
            break
    if n == 14:
        t = ''.join(cmds[:c])
        if '33' not in t:
            set_pgrms.add(t)
print(len(set_pgrms))
print(*sorted(set_pgrms), sep='\n')