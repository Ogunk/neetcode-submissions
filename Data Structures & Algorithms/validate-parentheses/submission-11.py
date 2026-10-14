class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        openingBrackets = ['(', '{', '[']
        closingBrackets = [')', '}', ']']
        stack = []

        for i in range(0, len(s)):
            if s[i] in openingBrackets:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                indexOpening = openingBrackets.index(stack[len(stack)-1])
                indexClosing = closingBrackets.index(s[i])
                if indexOpening == indexClosing:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

