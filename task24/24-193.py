with open('24-191.txt') as F:
    s = F.readline()

WAIT_A = 0
WAIT_B = 1
chunks = []
state = WAIT_A
for i, c in enumerate(s):
    if state == WAIT_A:
        if c == 'A':
            state = WAIT_B
            ch = ''
    elif state == WAIT_B:
        if c == 'B':
            if len(ch) >= 18:
                chunks.append(ch)
            state = WAIT_A
            ch = ''
        elif c == 'A':
            ch = ''
        else:
            ch += c

print(len(chunks))
# print( chunks )

s = open('24-191.txt').readline().split('A')[1:]
c = 0
for el in s:
    if len(el) >= 19 and el[-1] == 'B' and 'A' not in el and el.count('B') == 1:
        c += 1
print(c)
