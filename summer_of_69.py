"""
Return the sum of the numbers in the array, exceptignore sections of numbers starting with a 6 and extending to the next 9
(every 6 will be followed by atleast one 9). Return 0 if no numbers
summer_69([1,3,5]) --> 9
summer_69([4,5,6,8,9]) --> 9
summer_69([1,2,6,9,11]) --> 14
"""

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
    return total

n = int(input())
arr = []
for i in range(0,n):
    ip = int(input())
    arr.append(ip)

result = summer_69(arr)
print(result)
