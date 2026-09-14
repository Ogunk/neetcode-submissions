class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        result = []
        length = ""
        i = 0
        while i != len(s):
            if s[i] == "#":
                intLength = int(length)
                start = i+1
                finish = start + intLength
                result.append(s[start:finish])
                length = ""
                i = finish
                continue
            length += s[i]
            i += 1
        return result
