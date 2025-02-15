class MinStack(object):

    def __init__(self):
        self.stack=[]   

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # If stack is empty, the minimum is val itself
        current_min = val if not self.stack else min(val, self.stack[-1][0])
        self.stack.append((current_min, val))
    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack):
            self.stack.pop()
    
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1][1]
    
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1][0]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()