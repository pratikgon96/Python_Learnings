
A = [1,2,3,4]
C = []
B = []
def t_hanoi(n,A,C,B):
    if n == 1:
        C.append(A.pop())
    elif n > 1:
        t_hanoi(n-1,A,B,C)
        C.append(A.pop())
        t_hanoi(n-1,B,C,A)
    else:
        print("fuck off!")
t_hanoi(len(A),A,C,B)

print(A,C,B)
