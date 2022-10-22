from array import *

arr = array('i',[])

n = int(input('enter the lenght: '))
for i in range(n):
    x = int (input("enter the next value: "))
    arr.append(x)

print(arr)

val = int(input("enter the value to be searched: "))
k=0
for e in arr:
    if e==val:
        print(k)
        break

    k+=1

print(arr.index(val))  #function to search a value in araay