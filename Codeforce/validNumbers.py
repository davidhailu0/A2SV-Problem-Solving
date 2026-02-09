t = int(input())
for _ in range(t):
    n,m,p,q = map(int,input().split())
    flag = "YES"
    possible_sums = []
    for i in range(m):