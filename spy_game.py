"""
Write a function that takes a list of int and returns true if it contains 007 in order
list[1,5,0,0,7,9] --> True
list[3,0,6,0,1,8,7,4] --> True
list[7,9,0,2,0,3] --> False
"""

def spy_game(arr):
    code = [0,0,7,'\0']

    for j in arr:
        if j == code[0]:
            code.pop(0)
        else:
            pass
    return len(code) == 1

n = int(input())
arr = []
for i in range(0,n):
    ip = int(input())
    arr.append(ip)

result = spy_game(arr)
print(result)