from collections import defaultdict
from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_count = 0
        
        for i in points:
            distance_count = defaultdict(int)
            
            for j in points:
                if i == j:
                    continue
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist_sq = dx*dx + dy*dy
                distance_count[dist_sq] += 1
            for count in distance_count.values():
                if count > 1:
                    total_count += count * (count - 1)
        
        return total_count