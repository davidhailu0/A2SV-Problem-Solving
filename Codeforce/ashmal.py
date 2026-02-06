t = int(input())
for _ in range(t):
    n = int(input())
    string = input().split()
    s = ""
    temp = string[0].lower()
    for i in range(n):
        if string[i].lower() <= temp:
            s = string[i] + s
            temp = s[i].lower()
        else:
            s = s + string[i]
            temp = string[i].lower()
    print(s)