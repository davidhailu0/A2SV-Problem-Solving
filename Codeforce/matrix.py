col = -1
row = -1
for i in range(5):
    arr = input().split()
    if '1' in arr:
        col = arr.index('1')
        row = i
        break
print(abs(col - 2)+abs(row - 2))