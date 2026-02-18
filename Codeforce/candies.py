t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(-1)
        continue
    
    spells = []
    steps = 0
    while n > 1 and steps < 40:
        if (n + 1) % 2 == 0:  
            spells.append(1)
            n = (n + 1) // 2
        else: 
            spells.append(2)
            n = (n - 1) // 2
        steps += 1
    
    if n == 1:
        spells.reverse()
        print(len(spells))
        print(" ".join(map(str, spells)))
    else:
        print(-1)