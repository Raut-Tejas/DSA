class dequeue:
    def __init__(self):
        self.iteam=[]
    
    def isEmpty(self):
        return len(self.iteam)==0
    
    def insertatfront(self,value):
        self.iteam.insert(0,value)
        
    def deleteatfront(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            return self.iteam.pop(0)

    def insertatend(self,value):
        self.iteam.append(value)
        
    def deleteatend(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            return self.iteam.pop()
    
    def peekatfront(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            print(self.iteam[0])
        
    def peekatend(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            print(self.iteam[-1])

q1=dequeue()

q1.insertatfront(20)
q1.insertatfront(10)

q1.insertatend(30)
q1.insertatend(40)

Print("Elements Of Dequeue")
q1.peekatfront()
q1.peekatend()

print("Delete Elements In Dequeue")

print(q1.deleteatfront())
print(q1.deleteatend())

