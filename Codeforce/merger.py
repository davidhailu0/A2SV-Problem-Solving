t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    print(" ".join(result))