test_cases = int(input())

for _ in range(test_cases):
    length = int(input())
    string = list(input())
    result = "YES"
    index = length
    while index > 1:
        print(string[0:index])
        print(list(reversed(string))[0:index])
        print("*******************************")
        print(list(reversed(string))[length-index:length])
        print(string[length-index:length])
        if string[0:index] == list(reversed(string))[0:index] and length != 1:
            print("NO")
            result = "NO"
            break
        elif list(reversed(string))[length-index:length] == string[length-index:length] and length != 1:
            print("NO")
            result = "NO"
            break
        index -= 1
    if result != "NO":
        print("YES")


    

    