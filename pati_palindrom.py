n = int(input('enter the no: '))

ori_no = n
res_no = 0

while n != 0:
    rem = n % 10
    res_no = res_no * 10 + rem
    n = n//10

if ori_no == res_no:
    print("palindrome",res_no)

else:
    print('not palindrome: ',res_no)