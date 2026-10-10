#Stack Using Insert Function :

#Create Stack Using List
class stack :
    def  __init__(self):
        self.s=[]
    
    #find length of List 
    def length(self):
        return len(self.s)
    
    #push element using insert function
    def push(self,value):
        self.s.insert(0,value)
    
    #display top element
    def peek(self):
        if self.length() == 0:
            raise Exception("Stack Is Empty")
        else:
            return self.s[0]
    
    #pop a top element using pop function of list:
    def pop(self):
        if self.length() == 0:
            raise Exception("Stack Is Empty")
        else:
            return self.s.pop(0)

stk=stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
stk.push(50)
print(stk.peek())
print(" Pop elemets:  ")
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
