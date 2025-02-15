from queue import Queue

class MyStack(object):

    def __init__(self):
        self.queue=Queue()
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        s=self.queue.qsize()
        self.queue.put(x)
        for _ in range(s):
            self.queue.put(self.queue.get())


    def pop(self):
        """
        :rtype: int
        """
        if self.queue.empty():
            return -1
        self.queue.get()

    def top(self):
        """
        :rtype: int
        """
        if self.queue.empty() :
            return -1
        return self.queue.queue[0]
    

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue.qsize():
            return False
        return True
    def __repr__(self):
        s=self.queue.qsize()
        ans="stack"
        for i in range(s):
            ans+=f"->{self.queue.queue[i]}"
        return ans
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

q=MyStack()
for i in range(1,10):
    q.push(i)
q