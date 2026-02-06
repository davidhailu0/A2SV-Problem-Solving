t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    if string.__contains__("2026") or not string.__contains__("2025"):
        print(0)
    else:
        if string.__contains__("2025"):
            print(1)
        elif string.count("0") == len(string) - 1 or (string.__contains__("202") and len(string) > 3):
            print(1)

    