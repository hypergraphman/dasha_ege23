from itertools import product

def f1(n):
    return n + 1
def f2(n):
    return n * 2

n_cmd = ['1', '2']
pgrms = product(n_cmd, repeat=10)
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
        if n == 11:
            break
    if n == 11:
        t = ''.join(cmds[:c])
        if t.count('2') <= 2:
            set_pgrms.add(t)
print(len(set_pgrms))
print(*sorted(set_pgrms), sep='\n')