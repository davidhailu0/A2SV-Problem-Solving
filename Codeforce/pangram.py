length_of_string = len(input())
string = input()
if len(set(list(string.lower()))) == 26:
    print("YES")
else:
    print("NO")