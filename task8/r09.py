from itertools import permutations

alf = 'вуаль'
c = 0
for word in permutations(alf):
    word = ''.join(word)
    if word[0] != 'ь' and 'ьу' not in word and 'ьа' not in word:
        c += 1
print(c)