f = range(6)
print("list comp",end=':')
q = [x+2 for x in f]
print(q)
print("gen exp",end=':')
r = (x+2 for x in f)
print(r)
for x in r:
    print(x)