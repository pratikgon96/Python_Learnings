from numpy import *

arr1 = array([1,2,4,6,9])
arr2 = array([12,43,11,65])
arr = arr1 + 4

print(arr)
print(concatenate([arr1,arr2]))

arr3 = arr1.view() #shallow copy i.e change of any value of one array effects the other.
arr4 = arr1.copy() #deep copy i.e independent arrays with same value
print(arr1)
print(arr3)
print(id(arr3))
print(id(arr1))