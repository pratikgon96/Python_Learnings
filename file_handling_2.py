"""File handling ex1-write"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt",'w')
file.write("oop! overwritten\n")
file.close()

"""File handling ex2-write"""
import os
file = open("C:/Users/PRATIK GON/Desktop/imp.txt",'a')
file.write("still you are a sucker")
file.close()

"""File handling ex3-create"""
import os
file = open("C:/Users/PRATIK GON/Desktop/prat.txt",'w')
file.write("lord himself!")
file.close()

"""File handling ex4-deletion"""
import os
if os.path.exists("C:/Users/PRATIK GON/Desktop/prat.txt"):
    os.remove("C:/Users/PRATIK GON/Desktop/prat.txt")
else:
    print("fuck off!")