from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""]*len(s)
        for ind,char in zip(indices,s):
            result[ind] = char
        return "".join(result)