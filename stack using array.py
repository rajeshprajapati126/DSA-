#using array

class Stack:
    def __init__(self,max_size):
        self.max_size=max_size
        self.top=-1
        self.arr=[None]*max_size
    def top(self):
        if self.top==-1:
            raise "stack is Empty"
        return self.data[self.top]
    def push(self,data):
        if self.top==self.max_size-1:
            raise "stack is full"
        self.top=self.top+1
        self.arr[self.top]=data 
    def pop(self):
        if self.top==-1:
            raise "stack is empty"
        poped_data=self.arr[self.top]
        self.arr[self.top]=None 
        self.top=self.top-1
        return poped_data 
    def __repr__(self):
        ans="Stack("
        i=0
        while i!=self.top:
            ans+=f"{self.arr[i]},"
            i+=1
        return ans[:-1]+")"
s=Stack(10)

for i in range(10):
    s.push(i+1)
for i in range(5):
    s.pop()
print(s)