nums = []
for i in range(64444, 77563 + 1):
    d0 = i % 10
    d1 = i // 10 % 10
    d2 = i // 100 % 10
    d3 = i // 1000 % 10
    d4 = i // 10000
    if d0 % 2 != 0 and d1 % 2 != 0 and d2 % 2 != 0 and \
       i % 9 != 0 and i % 13 != 0 and i % 17 != 0 and \
       d3 % 2 == 0 and d4 % 2 == 0:
        nums.append(i)

print(len(nums), max(nums) - min(nums))