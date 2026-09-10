class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedWords = collections.defaultdict(list)
        for word in strs:
            lettersArray = [0] * 26
            for letter in word:
                lettersArray[ord(letter)-ord('a')] += 1
            key = tuple(lettersArray)
            groupedWords[key].append(word)
        return list(groupedWords.values())
