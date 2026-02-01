from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = set(range(0,len(nums)+1)) - set(nums)
        return list(result)[0]