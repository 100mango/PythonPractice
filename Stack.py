#coding=utf-8

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
        

#剑指offer 面试题22：栈的压入，弹出序列：
def isProperPopOrder(pushOrder,popOrder):

    if pushOrder is None or popOrder is None or len(pushOrder) != len(popOrder) :
        return False

    stack = []
    stack.append(pushOrder.pop(0))
    while stack:
        top = popOrder.pop(0)
        while pushOrder and stack[-1] != top:
            stack.append(pushOrder.pop(0))

        if stack[-1] != top:
            return False

        stack.pop()
        if len(pushOrder) > 0:
            stack.append(pushOrder.pop(0))

    return True


print isProperPopOrder([1,2,3,4,5],[4,5,3,2,1])

print isProperPopOrder(None,None)

