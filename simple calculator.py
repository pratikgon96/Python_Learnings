import math

print('\t_____CALCULATOR____')

def add(a,b):
    a = a+b
    return a

def sub(a,b):
    if a>b:
        a = a-b
        return a
    else:
        b = b-a
        return b

def mul(a,b):
    a = a*b
    return a

def div(a,b):
    q = a/b
    r = a%b
    print("the quotient is: ",q)
    print("the remainder is: ",r)

def sqr(a):
    x = math.sqrt(a)
    return x

def pwr(a):
    y = math.pow(a,2)
    return y


while 1:
    print("\nchoose the operation you want to perform: ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBSTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SQUARE ROOT")
    print("\n\t6.SQUARE")
    print("\n\t7.EXIT")

    choice = int(input('> '))

    if choice == 1:
        print('\nEnter the two numbers: ')
        num1 = int(input("> "))
        num2 = int(input('> '))
        s = add(num1,num2)
        print("the result is: ",s)

    elif choice == 2:
        print("\nenter the two numbers: ")
        num1 = int(input("> "))
        num2 = int(input('> '))
        m = sub(num1,num2)
        print("the result is: ",m)

    elif choice == 3:
        print("\nenter the two numbers: ")
        num1 = int(input("> "))
        num2 = int(input('> '))
        p = mul(num1, num2)
        print("the result is: ", p)

    elif choice == 4:
        print("\nenter the two numbers: ")
        num1 = int(input("> "))
        num2 = int(input('> '))
        d = div(num1, num2)

    elif choice == 5:
        print("\nenter the numbers: ")
        num1 = int(input("> "))
        r = sqr(num1)
        print("the result is: ", r)

    elif choice == 6:
        print("\nenter the numbers: ")
        num2 = int(input('> '))
        sq= pwr(num2)
        print("the result is: ", sq)


    else:
        print("\nExit")
        break