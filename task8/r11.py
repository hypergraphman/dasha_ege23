from itertools import product

alf = 'skalo'
c = 0
for word in product(alf, repeat=3):
    word = ''.join(word)
    if word.count('k') == 1:
        c += 1
print(c)