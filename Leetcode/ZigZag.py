def zigzag(string:str,numRows:int)->str:
    count = 0
    flag = False
    result = {}
    for i,char in enumerate(string):
        if count < numRows and not flag:
            decrease = 0 if i<numRows else (numRows-2)
            result[(i-decrease)%numRows] = result.get((i-decrease)%numRows,"") + char
            count += 1
            if count ==numRows:
                flag = True
                count -= 1
        else:
            count -= 1
            result[count] = result.get(count,"") + char
            if count==0:
                flag = False
                count = 0
        print(result)
    return "".join(result.values())

print(zigzag("ABCDEFG",3))