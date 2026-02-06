from collections import Counter
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        result = [num for num,freq in nums_counter.items() if freq>=2]
        return result