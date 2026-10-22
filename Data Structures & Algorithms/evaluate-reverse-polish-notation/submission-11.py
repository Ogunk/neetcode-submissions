class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []
        operations = ["+","-","*","/"]

        for i in range(0, len(tokens)):
            if tokens[i] not in operations:
                numberStack.append(int(tokens[i]))
            else:
                res = numberStack[len(numberStack)-2]
                numberTwo = numberStack[len(numberStack)-1]
                if tokens[i] == '+':
                    res += numberTwo
                if tokens[i] == '-':
                    res -= numberTwo
                if tokens[i] == '*':
                    res *= numberTwo
                if tokens[i] == '/':
                    res = int(res / numberTwo)
                numberStack.pop()
                numberStack.pop()
                numberStack.append(res)

        return numberStack[0]