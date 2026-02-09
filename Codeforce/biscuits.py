t = int(input())

for _ in range(t):
    biscuits = int(input())
    count = 0
    if biscuits % 2 == 0:
        print((biscuits//2)-1)
    else:
        print(biscuits//2)
