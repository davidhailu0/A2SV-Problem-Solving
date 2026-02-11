class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        for i in range(len(s)-1):
            # print(s.rfind(s[i]))
            # print(s[i] == s[s.rfind(s[i])])
            if i == s.rfind(s[i]) and len(palindrome)<1:
                palindrome = s[i]
            else:
                string = s
                count = string.count(s[i])
                while count>=2: 
                    last_i = s.rfind(s[i])
                    # print(last_i)
                    if s[i:last_i] == "".join(reversed(s[i:last_i])) and len(s[i:last_i])>len(palindrome):
                        palindrome = s[i:last_i]
                    string = string[0:last_i]
                    print(f"cutted String {string}")
                    count -= 1       
        return palindrome
        [].pop()
    

sol = Solution()
sol.longestPalindrome("acaa")