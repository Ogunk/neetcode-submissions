class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter, 0)+1
        for letter in t:
            letters[letter] = letters.get(letter, 0)-1
        
        for entry in letters:
            if letters[entry] != 0:
                return False
        return True