def f(n):
    count = 0
    for d in str(n):
        if int(d) * 197 == n:
            count += 1
    return count


a = [int(i) for i in open('17-298.txt')]
c = 0
for e in a:
    if e % 197 == 0 and e > c:
        c = e

ans1, ans2 = 0, 0
for i in range(len(a) - 1):
    x1, x2 = a[i], a[i + 1]
    if (f(x1) > 0 and f(x2) == 0 or f(x1) == 0 and f(x2) > 0) and x1 + x2 < c:
        ans1 += 1
        ans2 = max(x1 + x2, ans2)
print(ans1, ans2)
