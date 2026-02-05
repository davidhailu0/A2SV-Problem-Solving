t = int(input())
for _ in range(t):
    string = input()
    result = 0
    for i in range(len(string)):
        if string.count('s') == len(string):
            break
        elif i % 2 == 0 and string[i] != 's':
            if i < len(string) - 1 and string[i + 1] == 's' and (i+1) < len(string)-1:
                # print(i, string[i])
                result += 1
                modified_string = list(string)
                modified_string[i + 1] = 'u'
                modified_string[i] = 's'
                string = ''.join(modified_string)
            elif i < len(string)-1:
                modified_string = list(string)
                modified_string[i] = 's'
                string = ''.join(modified_string)
                # print(i, string[i])
                result += 1
        elif i % 2 != 0 and string[i] != 'u' and  len(string)-1:
            if i < len(string) - 1 and string[i + 1] == 'u' and (i+1) < len(string)-1:
                modified_string = list(string)
                modified_string[i + 1] = 's'
                modified_string[i] = 'u'
                string = ''.join(modified_string)
                result += 1
                # print(i, string[i])
            # elif :
            #     modified_string = list(string)
            #     modified_string[i] = 'u'
            #     string = ''.join(modified_string)
        elif i == len(string) - 1 and string[i] != 's':
            # print(i, string[i])
            result += 1
    # print(string)
    print(result)