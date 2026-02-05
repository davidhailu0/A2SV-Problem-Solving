t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    result = {}
    for i,value in enumerate(arr):
        if i%2 == 0:
            result[value] = "red"
        else:
            result[value] = "blue"
    arr.sort()
    prev = "black"
    val = "YES"
    for i in arr:
        if prev == result[i]:
            val = "NO"
        prev = result[i]
    print(val)
