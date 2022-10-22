n = int(input("enter the no of object you want to transfer: "))
def t_hanoi(n,A,C,B):
    if n == 1:
        print("move %i from tower %s to tower %s: " %(n,A,C))
    elif n > 1:
        t_hanoi(n-1,A,B,C)
        print("move %i from tower %s to tower %s: " %(n,A,C))
        t_hanoi(n-1,B,C,A)
    else:
        print("fuck off!")
t_hanoi(n,'A','C','B')

