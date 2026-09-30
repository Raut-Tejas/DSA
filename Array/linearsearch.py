from numpy import *
arr=array([])
n=int(input("Enter The Size Of Array : "))
for i in range(n):
    ele=(int(input("Enter The Next Element : ")))
    arr=append(arr,ele)
print(arr)

find=int(input("Enter The Searching Element : "))
for i in arr:
    if find==i:
        print("Element Are present")
        break

else:
    print("Element are not present")