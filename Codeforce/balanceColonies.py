t = int(input())

for _ in range(t):
    n = int(input())
    if n<=2:
        print(n)
    elif n%3==0 or n%2==0:
        print(0)
    else:
        diff_2 = 2-(n%2)
        diff_3 = 3-(n%3)
        if diff_2<diff_3:
            print(diff_2)
        else:
            print(diff_3)