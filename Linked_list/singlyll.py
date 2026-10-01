class node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class singlyll:
    def __init__(self,head=None):
        self.head=head

    #Insert Node at End 
    def insertatend(self,value):
        temp=node(value) #give values store the address in temp
        if(self.head != None): #check the LL are Empty or not
            t1=self.head        # declare assistent to forward , if Head not empty then assistent point the head loction and move forward
            while(t1.next !=None):  #to check assistent next are none or not if not then access the next node value
                t1=t1.next
            t1.next=temp    #if assistent have none values then give the temp loction value and link the list
        else:
            self.head=temp  #if head are empty then give a value from tem and create a node
    
    def printll(self):
        t1=self.head
        while(t1.next !=None):
            print(t1.data,end="->")
            t1=t1.next
        print(t1.data)

obj=singlyll()
obj.insertatend(10)
obj.insertatend(20)
obj.insertatend(30)
obj.insertatend(40)
obj.printll()