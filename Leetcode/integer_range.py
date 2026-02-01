from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for value in range(left,right+1):
            found_in_range = False
            for range_ in ranges:
                if range_[0]<= value <= range_[1]:
                    found_in_range = True
                    break
            if not found_in_range:
                return False
        return True