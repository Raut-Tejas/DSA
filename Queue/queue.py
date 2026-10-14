class Queue:
    def __init__(self):
        self.iteam=[]
        
    def isEmpty(self):
        return len(self.iteam)==0

    def insert(self,value):
        self.iteam.append(value)
    
    def delete(self):
        if self.isEmpty() :
            raise Exception("Queue Is Empty")
        else:
            return self.iteam.pop(0)
    
    def peek(self):
        if self.isEmpty() :
            raise Exception("Queue Is Empty")
        else:
           return self.iteam[0]

Q1=Queue()
print(Q1.isEmpty())

Q1.insert(10)
Q1.insert(20)
Q1.insert(30)
Q1.insert(40)

print(Q1.peek())

print(Q1.delete())
print(Q1.delete())
print(Q1.delete())
print(Q1.delete())