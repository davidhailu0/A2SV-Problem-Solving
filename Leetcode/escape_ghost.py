from typing import List
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        min_ghost_move = 10**10
        for i in range(len(ghosts)):
            move = abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1])
            if move < min_ghost_move:
                min_ghost_move = move
        min_move = abs(target[0]) + abs(target[1])
        return min_ghost_move > min_move


        