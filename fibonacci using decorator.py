n = int(input("enter the range: "))
def fib(n):
    x = 0
    f,s = 0,1
    while x<=n:
        yield f
        f,s = s,f+s
        x += 1
for i in fib(n):
    print(i)