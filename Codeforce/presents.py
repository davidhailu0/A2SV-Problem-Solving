number_of_friends = int(input())

gift_order = map(str,input().split())

friend_counter = 1
map_friends = {}
for which_friend in gift_order:
    map_friends[which_friend] = str(friend_counter)
    friend_counter += 1

output = ''
for ordered_friend in range(1,number_of_friends+1):
    output += map_friends[str(ordered_friend)]
    output += ' '

print(output.strip())
