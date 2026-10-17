#create Dequeue using List
class dequeue:
    def __init__(self):
        self.iteam=[]
    
    #Isempty Function 
    def isEmpty(self):
        return len(self.iteam)==0
    
    #insert/Delete At Front
    def insertatfront(self,value):
        self.iteam.insert(0,value)
        
    def deleteatfront(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            return self.iteam.pop(0)

    #insert/Delete At End
    def insertatend(self,value):
        self.iteam.append(value)
        
    def deleteatend(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            return self.iteam.pop()
    
    #peek function of front 
    def peekatfront(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            print(self.iteam[0])
    
    #peek function of End 
    def peekatend(self):
        if self.isEmpty():
            print("Dequeue Is Empty")
        else:
            print(self.iteam[-1])

#object of Class Q1
q1=dequeue()

#insert elemnts at front
q1.insertatfront(20)
q1.insertatfront(10)

#insert elemnts at End
q1.insertatend(30)
q1.insertatend(40)

#peek elements In queue
print("Elements Of Dequeue")
q1.peekatfront()
q1.peekatend()

#pop Elements in queue
print("Delete Elements In Dequeue")

print(q1.deleteatfront())
print(q1.deleteatend())

