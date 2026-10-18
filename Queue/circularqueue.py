class circular_queue:
    def __init__(self,size):
        self.size=size
        self.iteam=[None]*size
        self.front = self.rear = -1
        
    def isEmpty(self):
        return self.front ==-1 and self.rear ==-1
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self,value):
        if self.isFull():
            print("Queue Is Full")
        elif self.isEmpty():
            self.front = self.rear = 0  
            self.iteam[self.rear]=value
        else:
            self.rear= (self.rear + 1 ) % self.size
            self.iteam[self.rear]=value
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        elif self.front==self.rear:
            print(self.iteam[self.front])
            self.front = self.rear = -1
        else:
            print(self.iteam[self.front])
            self.front= (self.front + 1 ) % self.size
            
             
            
            
            
q1=circular_queue(5)
print(q1.isEmpty())
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.dequeue()
q1.enqueue(60)

print(q1.isFull())
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
