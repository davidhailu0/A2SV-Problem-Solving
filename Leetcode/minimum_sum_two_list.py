from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        smallest_sum = -1
        words = []
        for index,string in enumerate(list1):
            if string in list2:
                if (index + list2.index(string)) < smallest_sum or smallest_sum == -1:
                    smallest_sum = (index + list2.index(string))
                    words.clear()
                    words.append(string)
                elif (index + list2.index(string)) == smallest_sum:
                    words.append(string)
        return words
        



        