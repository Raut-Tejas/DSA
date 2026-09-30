#Array By Using Array Module 
# import array as arr
from array import *

#create print Array fun
def printarr(arr):
    for i in arr:
        print(i, end=" ")
    print("\n")
    

#get user inpute in array
arr=array('i',[])
n=int(input("Enter The value of Array : "))
for i in range(0,n):
    arr.append(int(input("Enter The Next Element : ")))

printarr(arr)

#copy and update array
copyarr1=array(arr.typecode,(x for x in arr))
copyarr1.insert(3,55)
copyarr1.append(100)
copyarr1[3]=600
printarr(copyarr1)

#delete array element
copyarr2=array(arr.typecode,(x for x in arr))
copyarr2.pop(3) #delete at position
copyarr2.pop() #LIFO dehevior like stack
copyarr2.remove(10) #delete at value in array
printarr(copyarr2)

#slicing
print(arr[0:-2])


# find Element in Array
i=arr.index(30)
print(i)
