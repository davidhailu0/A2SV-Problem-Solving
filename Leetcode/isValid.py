class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for char in s:
            if len(result) == 0 and (char == ")" or char == "]" or char == "}"):
                return False
            elif char == ")" and result[-1]=="(":
                result.pop()
            elif char == "]" and result[-1]=="[":
                result.pop()
            elif char == "}" and result[-1]=="{":
                result.pop()
            else:
                result.append(char)
        return len(result)==0 

sol = Solution()
print(sol.isValid("(])"))