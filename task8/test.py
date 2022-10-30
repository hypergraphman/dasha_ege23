from itertools import product

alf = '123'
for word in product(alf, repeat=3):
    word = ''.join(word)
    f = not(word[0] == word[1] and word[1] == word[2] and word[0] == word[2])
    print(word, f)