from itertools import permutations

alf = 'kkaapn'
words = set()
for word in permutations(alf):
    word = ''.join(word)
    if 'kk' not in word and 'aa' not in word:
        words.add(word)
print(len(words))
