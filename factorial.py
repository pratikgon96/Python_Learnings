n = int(input("enter the no to be evaluated: "))

def fact(n):
    res = 1
    if n==0:
        print(res)
    elif n < 0:
        print("fuck off")
    else:
        for i in range(1,n+1):
            res = res * i

        print(res)

fact(n)