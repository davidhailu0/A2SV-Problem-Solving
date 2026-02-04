from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = list(words[0])
        for word in words:
            for letter in list(words[0]):
                if letter not in word:
                    while result.count(letter)!=0:
                        result.remove(letter)
                elif letter in word and result.count(letter)>word.count(letter):
                    while result.count(letter)>word.count(letter):
                        result.remove(letter)
        return result