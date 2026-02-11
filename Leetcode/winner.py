class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num = [True]*(n)
        head = 0
        while num.count(True)>1:
            counter = 0
            while k-1 >counter:
                counter += 1
                head += 1
            if head >= len(num):
                head %= len(num)
            num[head] = False
            head += 1
            print(num)
        return num.index(True)+1
sol = Solution()
print(sol.findTheWinner(5,2))