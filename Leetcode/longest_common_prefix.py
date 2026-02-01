from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        shortest_string_length = min([len(string) for string in strs])
        count = 0
        while count < shortest_string_length:
            prefix = strs[0][0:count+1]
            for string in strs:
                if not string.startswith(prefix):
                    return common_prefix
            common_prefix = prefix
            count += 1
        return common_prefix