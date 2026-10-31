def sumarray(arr):
    
    if not arr:
        return 0
    return  arr[0] + sumarray(arr[1:])  #Create a recursion with add first element and get recursion so this create new array with calling recursion function      
    
x=[1,2,3,4,5]
print(sumarray(x))