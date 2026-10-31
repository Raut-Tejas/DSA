def printno(Lrange,Urange):
    if Lrange > Urange :
        return 
    print(Lrange)
    printno(Lrange+1, Urange)
    
x=int(input("Enter The Lower Range : "))
y=int(input("Enter THe Upper Range : "))
printno(x,y)