contestants , k = map(int, input().split(' '))
count = 0
result = list(map(int, input().split(' ')))
for i in range(contestants):
    if result[i]>= result[k-1] and result[i]>0:
        count += 1
print(count)