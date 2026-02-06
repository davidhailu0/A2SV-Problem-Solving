from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        if len(s) != len(t):
            return False
        for char,freq in s_counter.items():
            if freq != t_counter[char]:
                return False
        return True