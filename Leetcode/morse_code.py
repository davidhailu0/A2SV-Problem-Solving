from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        concatenated = ",".join(words)
        converted = ""
        for char in concatenated:
            if char == ",":
                converted += ","
            else:
                converted += morse_codes[ord(char)-ord('a')]
        return len(set(converted.split(',')))