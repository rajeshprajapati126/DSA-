# class queue:
#     def __init__(self,size):
#         self.front=-1
#         self.rear=-1
#         self.cnt=0
#         self.max_size=size
#         self.arr=[-1 for i in range(size)]
#     def push(self, x):
#         if self.cnt == self.max_size:
#             return -1  # Queue is full

#         self.rear = (self.rear + 1) % self.max_size
#         self.arr[self.rear] = x
#         self.cnt += 1

#         if self.front == -1:  # First element being inserted
#             self.front = 0
#     def pop(self):
#         if self.cnt==0:
#             return -1
#         dl=self.arr[self.front]
#         self.arr[self.front]=-1
#         self.front=(self.front+1)%(self.max_size)
#         self.cnt-=1
#         return dl
#     def top(self):
#         if self.cnt==0:
#             return -1
#         return self.arr[self.front]

# without using cnt variable

class queue:
    def __init__(self,size):
        self.front=-1
        self.rear=-1
        self.max_size=size
        self.arr=[-1 for i in range(size)]
    def push(self, x):
        if (self.rear+1)%self.max_size == self.front:
            print("FULL STACK")
            return # Queue is full
        self.rear = (self.rear + 1) % self.max_size
        self.arr[self.rear] = x
        if self.front==-1 and self.rear!=-1:
            self.front=0 
    def pop(self):
        if self.front == -1:  # Queue is empty
            return -1
        
        dl = self.arr[self.front]
        self.arr[self.front] = -1

        if self.front == self.rear:  # If only one element was present
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size

        return dl
    def top(self):
        if self.cnt==0:
            return -1
        return self.arr[self.front]
    def __repr__(self):
        if self.front == -1:
            return "Queue()"

        temp = self.front
        ans = "Queue("
        while temp != self.rear:
            ans += f"{self.arr[temp]}, "
            temp = (temp + 1) % self.max_size
        ans += f"{self.arr[temp]})"  # Add the last element
        return ans
    def get_front(self):
        return f"Front Element->{self.arr[self.front]}"
    def get_rear(self):
        return f"Rear Element->{self.arr[self.rear]}"

q1=queue(10)
for i in range(5):
    q1.push(i)
print(q1)
for i in range(3):
    q1.pop()
print(q1)
for i in range(5,14,4):
    q1.push(i)
print(q1)
print(q1.get_front(),q1.get_rear())
print(q1.pop())
q1.push(1)
print(q1)
q1.push(2)
q1.push(4)
q1.push(3)
q1.push(1)
q1.push(4)
print(q1)
print(q1.get_rear())
q1.push(50)
print(q1)


