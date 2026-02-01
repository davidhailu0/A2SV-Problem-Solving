number_of_test_cases = int(input())
for test_case in range(number_of_test_cases):
    first_input = input().split(' ')
    number_of_monster = first_input[0]
    bullets_fired = int(first_input[1])
    health_of_monsters = list(map(int,input().split(' ')))
    position_of_monsters = list(map(lambda x:abs(int(x)),input().split()))
    while 0 not in position_of_monsters:
        index_closest = position_of_monsters.index(min(position_of_monsters))
        while bullets_fired!=0:
            if bullets_fired<=health_of_monsters[index_closest]:
                health_of_monsters[index_closest] -= bullets_fired
                bullets_fired = 0
            else:
                health_of_monsters[index_closest] = 0
                bullets_fired -= health_of_monsters[index_closest]
                index_closest = position_of_monsters.index(min(position_of_monsters))
        position_of_monsters = list(map(lambda x: x - 1,position_of_monsters))
        print(f"Debug: {position_of_monsters}, {health_of_monsters}, bullets left: {bullets_fired}")
    if 0 in position_of_monsters:
        print("NO")
    else:
        print("YES")
