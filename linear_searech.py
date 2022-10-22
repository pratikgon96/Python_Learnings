pos = -1
def linear(list,num):
    i = 0

    while i < len(list):
        if list[i] == num:
           globals()['pos'] = i
           print("value found at: ",i+1)
           return True
        i = i+1
list = [2,5,9,3,6,7]
num = 7
if linear(list,num):
    print("Thank you",pos+1)
else:
    print("Not found")