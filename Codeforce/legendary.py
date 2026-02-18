t = int(input())
for _ in range(t):
    length = int(input())
    arr_input = list(map(int,input().split()))
    arr = [0 for _ in range(length)]
    op = 0
    average = sum(arr_input)//length
    for i in range(length):
        arr[i] = average
    op = 1
    while True:
        all_match = True
        for i in range(length):
            if arr[i] == arr_input[i]:
                arr[i] = 0
        min_ = min(arr_input)
        for i in range(length):
            if (arr_input[i]+min_)>arr_input[i]:
                arr[i] = 0 

        