from numpy import *

arr1 = array ([1,2,3])

arr2 = arr1.copy()

arr1[1]=0
arr1[2]=4

print(arr1)
print(arr2)

print(id(arr1))

print(id(arr2))