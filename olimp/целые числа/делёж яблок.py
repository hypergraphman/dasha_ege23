pupils, apples = map(int, input().split())
a = apples // pupils
left = apples % pupils
sad = (pupils - left) % pupils
print(a, left, sad)
