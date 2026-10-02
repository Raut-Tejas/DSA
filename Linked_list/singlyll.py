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
    
    #Insert At Begining
    def insertatbeg(self,value):
        temp=node(value)   #create a node with point a temp
        temp.next=self.head  #temp get a head location 
        self.head=temp      #head get temp first node location 

    #insert at Middele value
    def insertatmid(self,value,x):
        temp=node(value)   
        t1=self.head  
        while(t1.next != None):
            if(t1.data==x):
                temp.next=t1.next   #give a last node address to new node 
                t1.next=temp        #give new node address to value node next
            t1=t1.next      #if condition not run then t1 goto next node

    #Delete node at value
    def deleteLL(self,value):
        t1=self.head
        prev=t1
        while(t1.next!=None):
            if(t1.data == value):
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next

    #Print LL
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
obj.insertatbeg(5)
obj.insertatbeg(0)
obj.insertatmid(25,20)
obj.insertatmid(35,30)
obj.deleteLL(35)

obj.printll()