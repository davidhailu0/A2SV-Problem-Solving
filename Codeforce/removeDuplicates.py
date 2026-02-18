from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head = 0
        if len(nums)-1 == 1:
            return 1

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]: 
                head += 1 
                nums[head] = nums[i] 

        return head

sol = Solution()
sol.removeDuplicates([1,1,2])