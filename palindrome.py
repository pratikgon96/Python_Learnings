num = input("enter: ")
def pal(num):
    x1 = num[::-1] #reverse the num input

    if x1 == num:
        print('palindrom')
    else:
        print('not palindrome')

pal(num)