#leetcode minStack
class MinStack:
    def __init__(self):
        self.dataStack = []
        self.minStack = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.dataStack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1] > x:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    # @return nothing
    def pop(self):
        self.dataStack.pop()
        self.minStack.pop()
        
    # @return an integer
    def top(self):
        return self.dataStack[-1]

    # @return an integer
    def getMin(self):
        return self.minStack[-1]
        