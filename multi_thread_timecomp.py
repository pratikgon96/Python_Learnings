import time

def d2(n):
    for x in n:
        time.sleep(1)
        print(x%2)

def d3(n):
    for x in n:
        time.sleep(1)
        print(x%3)

n = [2,3,4,5,6,7,8,9]

s = time.time()
d2(n)
d3(n)
e = time.time()
print(e-s)

