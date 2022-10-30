start, end = 586132, 586430

minDivs = []
maxDivs = []
for x in range(start, end + 1):
    divs = [1, x]
    d = 2
    while d * d <= x:
        if x % d == 0:
            divs.append(d)
            if x // d > d:
                divs.append(x // d)
        d += 1
    divs = sorted(divs)
    if len(divs) >= len(maxDivs):
        maxDivs = divs
        if len(divs) > len(minDivs):
            minDivs = divs

print(len(minDivs), minDivs[-1], minDivs[-2])
print(len(maxDivs), maxDivs[-1], maxDivs[-2])
