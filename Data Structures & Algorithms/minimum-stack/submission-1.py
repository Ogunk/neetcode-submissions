class MinStack:
    def __init__(self):
        self.stack = []
        self.minValue = None

    def push(self, val: int) -> None:
        if self.minValue == None:
            self.minValue = val
        else:
            if val < self.minValue:
                self.minValue = val
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.minValue = None
        else:
            self.minValue = min(self.stack)

    def top(self) -> int:
        lastElementIndex = len(self.stack) - 1
        return self.stack[lastElementIndex]

    def getMin(self) -> int:
        return self.minValue
