from numpy import *
arr1 = array([
            [1,2,3,9,7,11],
            [4,5,6,8,10,14]

            ])

arr2 = arr1.flatten()
print(arr2)
#arr3 = arr2.reshape(2,3)
arr4 = arr2.reshape(2,2,3)
print(arr4)
#print(arr3)
print(arr1.shape)
print(arr1.ndim)
print(arr1.size)
