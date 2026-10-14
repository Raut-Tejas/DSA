# create Queue

class Queue:
    def __init__(self):  #create empty list using constructor
        self.iteam=[]
        
    #isEmpty function check queue is empty or not    
    def isEmpty(self):
        return len(self.iteam)==0

    #insert at end 
    def insert(self,value):
        self.iteam.append(value)
    
    #delete at first
    def delete(self):
        if self.isEmpty() :
            raise Exception("Queue Is Empty")
        else:
            return self.iteam.pop(0)
    
    #display a First Element
    def peek(self):
        if self.isEmpty() :
            raise Exception("Queue Is Empty")
        else:
           return self.iteam[0]

Q1=Queue()

print("Check Queue Is Empty :",Q1.isEmpty(),end="\n\n")
Q1.insert(10)
Q1.insert(20)
Q1.insert(30)
Q1.insert(40)
print("First Element:",Q1.peek(),end="\n\n")
print("Pop Elements :",end="\n")
print(Q1.delete())
print(Q1.delete())
print(Q1.delete())
print(Q1.delete())