t = int(input())

for _ in range(t):
    length = int(input())
    arr = list(map(int, input().split()))
    compare = list(range(length))
    set_arr =  set(compare) - set(arr)
    print(max(set_arr))