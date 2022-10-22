def great():
    print("hello")
    print("good morning")

great()

def add(x,y):
    c = x + y
    print(c)
    return c
add(5,7) # no return
result = add(9,4) #return something
print(result)

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d
result1, result2 = add_sub(9,4)
print(result1,result2)

