class queue:
    def __init__(self,size):
        self.front=-1
        self.rear=-1
        self.cnt=0
        self.max_size=size
        self.arr=[-1 for i in range(size)]
    def push(self, x):
        if self.cnt == self.max_size:
            return -1  # Queue is full

        self.rear = (self.rear + 1) % self.max_size
        self.arr[self.rear] = x
        self.cnt += 1

        if self.front == -1:  # First element being inserted
            self.front = 0
    def pop(self):
        if self.cnt==0:
            return -1
        dl=self.arr[self.front]
        self.arr[self.front]=-1
        self.front=(self.front+1)%(self.max_size)
        self.cnt-=1
        return dl
    def top(self):
        if self.cnt==0:
            return -1
        return self.arr[self.front]
q1=queue(5)
for i in range(5):
    q1.push(i)
while True:
    dl=q1.pop()
    if dl==-1:
        break
    print(dl)