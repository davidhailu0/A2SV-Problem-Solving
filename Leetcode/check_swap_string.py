class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_ = sorted(list(s1))
        s2_ = sorted(list(s2))
        if "".join(s1_) != "".join(s2_):
            return False
        different_index = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                different_index += 1
        return different_index<=2

        