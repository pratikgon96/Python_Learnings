
n = int(input("enter the no: "))
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)





res = fact(n)
print(res)