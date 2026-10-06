#creatre a code with there requrement None

class node:
    def __init__(self,value=None):
        self.data=value
        self.prev=None
        self.next=None

#create a list 
class doublell:
    def __init__(self):
        self.head=None   #initailze a head with none 

    #insert at End 
    def insertatend(self,value):
        temp=node(value)         #create a code with give a input value
        t=self.head              #for ieration give a dummi variable        
        if(self.head == None):   #check a any node present at first if not the create a and add in list and give a return there value
            self.head=temp 
            return
        while(t.next != None):  #if first node create and add more nodes the check last node
            t=t.next
        t.next=temp     #get a loction of temp node and give last node location to temp.prev node 
        temp.prev=t
        
        #insert at middle of value
    def insertatmid(self,value,x):
        temp=node(value)
        t=self.head
        while(t.next != None):
            if(t.data == x):
                temp.next=t.next
                t.next.prev=temp    
                t.next=temp
                temp.prev=t
                break
            else:
                t=t.next
    
    #insert at Begining
    def insertatbegi(self,value):
        temp=node(value)
        if(self.head == None):
            self.head=temp
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp    
    
            
    def printdll(self):
        t=self.head
        while(t.next != None):
            print(t.data ,end=" <--> ")
            t=t.next
        print(t.data)

obj=doublell()
obj.insertatend(10)
obj.insertatend(20)
obj.insertatend(30)
obj.insertatend(40)
obj.insertatbegi(5)
obj.insertatmid(35,30)
obj.printdll()