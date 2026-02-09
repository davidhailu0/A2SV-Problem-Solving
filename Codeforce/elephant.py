x = int(input())
steps = 0

if x >= 5:
    steps += (x // 5)
    x = x % 5
if x!=0:
    steps += 1
print(steps)