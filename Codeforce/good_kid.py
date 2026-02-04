test_case = int(input())
for _ in range(test_case):
    length = int(input())
    array = list(map(int,input().split()))
    minimum = min(array)
    product = 1
    add_one = 1
    for num in array:
        if num != minimum:
            product *= num
        else:
            product *= (num+add_one)
            add_one = 0
    print(product) 