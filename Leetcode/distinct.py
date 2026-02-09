from typing import List
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_counts = {}
        distinct = 0
        result = []
        for x,y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                color_counts[old_color] -= 1
                if color_counts[old_color] == 0:
                    distinct -= 1
            color_counts[y]= color_counts.get(y,0) + 1
            ball_colors[x] = y
            if color_counts[y]==1:
                distinct +=1 
            result.append(distinct)
        return result