from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        str1 = set("qwertyuiop")
        str2 = set("asdfghjkl")
        str3 = set("zxcvbnm")
        ans = []
        for string in words:
            sorted_string = set(string.lower())
            if set(sorted_string).issubset(str1):
                ans.append(string)
            elif set(sorted_string).issubset(str2):
                ans.append(string)
            elif set(sorted_string).issubset(str3):
                ans.append(string)
        return ans 

sol = Solution()
print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))