a = [0] * 10000
a[1] = 1
for i in range(1, 10):
    if i + 1 <= 10:
        a[i + 1] += a[i]
    if i * 2 <= 10:
        a[i * 2] += a[i]

for i in range(10, 35):
    if i + 1 <= 35 and i + 1 != 17:
        a[i + 1] += a[i]
    if i * 2 <= 35 and i * 2 != 17:
        a[i * 2] += a[i]
print(a[35])