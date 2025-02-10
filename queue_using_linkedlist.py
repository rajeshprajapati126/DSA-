

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def top(self):
        pass
    def push(self,data):
        temp=Node(data)
        
        if self.front==None:
            self.front=temp 
            self.rear=self.front

        else:
            self.rear.next=temp
            self.rear=temp 
    def pop(self):
        if self.front==None:
            return -1
        else:
            temp=self.front
            self.front=temp.next
            if self.front==None:
                self.rear=None 
        return temp.data
    def __repr__(self):
        temp=self.front
        queue=""
        while temp!=None:
            
            queue=queue+f"{temp.data}->"
            temp=temp.next
        queue=queue[:-2]
        return queue
q1=Queue()
for i in range(10,100,10):

    q1.push(i)
for i in range(1,11):

    (q1.pop())
print(q1.rear)


