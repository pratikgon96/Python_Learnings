pos = -1
def binary(list,num):
    lb = 0
    ub = len(list) - 1

    while lb <= ub:
        mid = (lb+ub)//2
        if list[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < num:
                lb = mid + 1
            else:
                ub = mid - 1
    return False


list = [2,3,5,6,7,9,15,34,39,65,122]
num = int(input("enter the no to be searched: "))
res = binary(list,num)
if binary(list,num):
    print("found",pos+1)
else:
    print("Not found")