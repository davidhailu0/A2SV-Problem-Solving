from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        more_than = len(nums)/3
        result = []
        counter_num = Counter(nums)
        for elem,freq in counter_num.items():
            if freq > more_than:
                result.append(elem)
        return result