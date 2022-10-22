"""File Handling ex1"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt.txt",'w')
file.close()

"""File handling ex2"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt",'r')
print(file.read())
file.close()

"""File handling ex3"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt",'r')
print(file.read(7))
file.close()

"""File handling ex4"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt",'r')
print(file.readline())
file.close()

"""File handling ex5"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt",'r')
print(file.readlines())
file.close()

"""File handling ex6- for loop"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt",'r')
for line in file:
    print(file.readlines())
file.close()