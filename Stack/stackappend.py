class stack:
    def __init__(self):
        self.s=[]
    
    def lenth(self):
        return len(self.s)
    
    def push(self,value):
        self.s.append(value)
        
    def peek(self):
        if self.lenth() ==0:
            raise Exception("Stack Is Empty")
        else:
            return self.s[-1]
        
    def pop(self):
        if self.lenth() ==0:
            raise Exception("Stack Is Empty")
        else:
           return self.s.pop(-1)

stk=stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
print(stk.peek())
print("Pop elements: ")
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())