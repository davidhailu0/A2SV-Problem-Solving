from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_num = Counter(nums)
        more_than = len(nums)//2
        results = []
        for elem,freq in counter_num.items():
            if freq > more_than:
                results.append(elem)
        return max(results)