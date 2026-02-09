num = int(input())
string = input()
result = []
if num < 0:
    print(0)
else:
    for i in range((len(string)%4)+1):
        try_outs_string = string[i:i+4]
        result.append(0)
        for index,char in enumerate(try_outs_string):
            if index == 0:
                result[i] += min(abs(ord(char)-ord("A")),91-ord(char))
            elif index == 1:
                result[i] += min(abs(ord(char)-ord("C")),91-ord(char))
            elif index == 2:
                result[i] += min(abs(ord(char)-ord('T')),91-ord(char))
            elif index == 3:
                result[i] += min(abs(ord(char)-ord('G')),91-ord(char))
    print(min(result))


