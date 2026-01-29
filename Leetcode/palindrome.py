class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x =  ''
        string_x = str(x)
        length_x_max_index = len(string_x) - 1
        while length_x_max_index > -1:
            reverse_x += string_x[length_x_max_index]
            length_x_max_index -= 1
        return string_x == reverse_x

s = Solution()
print(s.isPalindrome(121))