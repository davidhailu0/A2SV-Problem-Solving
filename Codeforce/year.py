year = int(input())

next_year = year + 1
while len(set(str(next_year))) != 4:
    next_year += 1
print(next_year)