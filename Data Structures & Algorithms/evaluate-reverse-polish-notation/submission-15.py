class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []

        for token in tokens:
            if token in "+-*/":
                a = numberStack.pop()
                b = numberStack.pop()
                if token == '+':
                    b += a
                elif token == '-':
                    b -= a
                elif token == '*':
                    b *= a
                else:
                    b = int(b / a)
                numberStack.append(b)
            else:
                numberStack.append(int(token))

        return numberStack[0]