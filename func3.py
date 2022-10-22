def sum(a,*b): # for using multiple values we use b as tuple.
    c =a
    for i in b:
        c = c + i
    print(c)

sum(5,6,87,33)

def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person('pratik',age=24,city='kolkata',mob=8967763126)