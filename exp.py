import math
f1 = lambda a,b: a+b
#f2 = lambda a,b:
f3 = lambda a,b:a*b
f4 = lambda a,b: a/b
f5 = lambda a: math.sqrt(a)
f6 = lambda a: math.pow(a,2)

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
        #s = add(num1,num2)
        s = f1(num1,num2)
        print("the result is: ",s)

    elif choice == 2:
        print("\nenter the two numbers: ")
        num1 = int(input("> "))
        num2 = int(input('> '))
        m = f2(num1,num2)
        print("the result is: ",m)

    elif choice == 3:
        print("\nenter the two numbers: ")
        num1 = int(input("> "))
        num2 = int(input('> '))
        p = f3(num1, num2)
        print("the result is: ", p)

    elif choice == 4:
        print("\nenter the two numbers: ")
        num1 = int(input("> "))
        num2 = int(input('> '))
        d = f4(num1, num2)

    elif choice == 5:
        print("\nenter the numbers: ")
        num1 = int(input("> "))
        r = f5(num1)
        print("the result is: ", r)

    elif choice == 6:
        print("\nenter the numbers: ")
        num2 = int(input('> '))
        sq= f6(num2)
        print("the result is: ", sq)


    else:
        print("\nExit")
        break