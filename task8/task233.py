from itertools import product

alf = '012345678'
c = 0
for word in product(alf, repeat=7):
    word = ''.join(word)
    if word[0] not in '0246' and (word[4] != word[5] or word[5] != word[6] or word[4] != word[6]):
        c += 1
print(c)