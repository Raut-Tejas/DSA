#create node
class node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next


#create single node with pointer head
class singlyll:
    def __init__(self,head=None,last=None):
        self.head=head
        self.last=self.head

    #Insert Node at End 
    def insertatend(self,value):

        temp=node(value) # give values store the address in temp

        if(self.head != None): # check the LL are Empty or not

            self.last.next=temp   # last node points to new node
            temp.next=self.head    # new node points to head

            self.last=temp         # update last node

        else:
            self.head=temp        # if head is empty then create first node
            self.last=temp        # first node is also the last node

            temp.next=self.head    # last node points to head


    #display
    def display(self):

        if(self.head == None):
            print("Linked List is Empty")
            return

        t1=self.head

        while True:
            print(t1.data,end=" -> ")
            t1=t1.next

            if(t1 == self.head):
                break

        print("(Head)")


l1=singlyll()

l1.insertatend(10)
l1.insertatend(20)
l1.insertatend(30)
l1.insertatend(40)

l1.display()
