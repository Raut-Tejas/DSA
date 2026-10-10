#Stack Using Append() Function

#create Stack Using Linst
class stack:
    def __init__(self):
        self.s=[]
    
    #find length of List
    def lenth(self):
        return len(self.s)
    
    #push element using insert function
    def push(self,value):
        self.s.append(value)
    
    #display top element using Negative index  -1 because we use append     
    def peek(self):
        if self.lenth() ==0:
            raise Exception("Stack Is Empty")
        else:
            return self.s[-1]
    
    #pop a top element using pop function of list    
    def pop(self):
        if self.lenth() ==0:
            raise Exception("Stack Is Empty")
        else:
           return self.s.pop()

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