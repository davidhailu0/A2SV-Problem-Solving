t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    op = 0
    if n != 1:
        for i in range(n-1):
            if arr[i]%2 == arr[i+1]%2:
                op += 1
    print(op)
    