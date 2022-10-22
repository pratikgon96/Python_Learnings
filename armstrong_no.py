import math
n = int(input("enter the no: "))

ori_no = n
res_no = 0

while n != 0:
    rem = n % 10
    res_no = res_no + pow(rem,3)
    n = n//10

if ori_no == res_no:
    print("Armstrong")

else:
    print("not armstrong")