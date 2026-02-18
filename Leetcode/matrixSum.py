from typing import List
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        max_ = [0]*len(nums)
        for num in range(len(nums)*len(nums[0])):
            ind = num%len(nums)
            if ind == 0:
                score += max(max_)
                max_ = [0]*len(nums)
            max_num = max(nums[ind])
            max_[ind] = max_num
            nums[ind].remove(max_num)
        score += max(max_)
        return score

sol = Solution()
sol.matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]])