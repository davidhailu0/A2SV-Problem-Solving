problems = int(input())
result = 0
for _ in range(problems):
    line_of_numbers = map(int,input().split(' '))
    total =sum(line_of_numbers)
    result += 1 if total >1 else 0 
print(result)