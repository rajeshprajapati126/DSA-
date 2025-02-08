class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class Stack:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        if self.top==None:
            return True
        return False 
    def top(self):
        if self.top==None:
            return -1 
        return self.top.data
    def push(self,data):
        if self.top==None:
            self.top=Node(data)
        else:
            temp=Node(data)
            temp.next=self.top
            self.top=temp 
    def __repr__(self):
        ans="Stack("
        
        temp=self.top 
        while temp:
            ans+=f"{temp.data},"
            temp=temp.next
        ans=ans[:-1]+")"
        return ans
    def pop(self):
        if self.isEmpty():
            raise "Empty Stack"
        temp=self.top 
        self.top=self.top.next
        temp.next=None 
        return temp.data
s=Stack()
for i in range(10):
    s.push(i)
print(s)
for i in range(5):
    print(s.pop())