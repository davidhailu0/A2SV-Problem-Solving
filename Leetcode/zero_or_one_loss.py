from collections import Counter
from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = Counter()
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1

        all_wins = sorted([p for p in players if loss_count[p] == 0])

        one_loss = sorted([p for p in players if loss_count[p] == 1])

        return [all_wins, one_loss]