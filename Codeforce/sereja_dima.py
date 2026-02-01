from collections import deque
number_of_cards = int(input())
cards = list(map(int,input().split(' ')))

total_sereja = 0
total_dima = 0
for round_ in range(number_of_cards):
    if cards[-1] > cards[0]:
        if round_%2 == 0:
            total_sereja += cards[-1]
        else:
            total_dima += cards[-1]
        cards.pop()
    else:
        if round_%2 == 0:
            total_sereja += cards[0]
        else:
            total_dima += cards[0]
        cards.pop(0)
print(total_sereja,total_dima,sep=' ')