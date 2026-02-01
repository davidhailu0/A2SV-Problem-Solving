from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self,a, b):
        count_a = Counter(a)
        count_b = Counter(b)
    
        for elem, freq in count_b.items():
            if count_a[elem] < freq:
                return False
        return True