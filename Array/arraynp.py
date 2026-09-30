# Array With Using Numpy Library
from numpy import *
arr=array([1,2,3,4,5])
print("Array:")
for i in arr:
    print(i, end=" ")
print("\n")


# Numeric arrays function in Numpy
print("Numeric arrays function in Numpy : ")
arr1=linspace(0,10,11)
print("linspace : ",arr1)

arr2=arange(0,10,2)
print("arange : ",arr2)

arr3=logspace(0,10,5)
print("Logspace : ",arr3)

arr4=zeros(10)
print("Zero elements : ",arr4)

arr5=ones(5)
print("1 Elements : ",arr5)

arr6=full(10,9)
print("Any Elements Array : ",arr6)
print("\n")
print("\n")

#Multidaimentional Array
print("Multidaimentional Array : ")
zero=array(10)
print("Zero Dimentional array:")
print(zero)
print("\n")

one=array([1,2,3,4,5])
print("One Dimentional array:")
print(one)
print("\n")

two=array([[1,2,3],[4,5,6],[7,8,9]])
print("Two Dimentional array:")
print(two)
print("\n")

three=array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Three Dimentional array:")
print(three)
print("\n")