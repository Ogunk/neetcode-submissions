class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []
        operations = ["+","-","*","/"]

        for i in range(0, len(tokens)):
            if tokens[i] not in operations:
                numberStack.append(int(tokens[i]))
            else:
                a = numberStack.pop()
                b = numberStack.pop()
                if tokens[i] == '+':
                    b += a
                if tokens[i] == '-':
                    b -= a
                if tokens[i] == '*':
                    b *= a
                if tokens[i] == '/':
                    b = int(b / a)
                numberStack.append(b)

        return numberStack[0]