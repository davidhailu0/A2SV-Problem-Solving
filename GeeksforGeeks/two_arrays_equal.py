class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        for index in range(len(sorted_a)):
            if sorted_a[index] != sorted_b[index]:
                return False
        return True