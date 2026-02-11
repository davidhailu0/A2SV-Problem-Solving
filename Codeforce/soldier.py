k,n,w = map(int,input().split())

total_cost = 0
for i in range(w):
    total_cost += ((i+1)*k)
print(total_cost-n if total_cost>n else 0)

hello = {}
len(hello.pop()