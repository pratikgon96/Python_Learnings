from functools import reduce
# filter() func within map func
c = map(lambda x: x+x, filter(lambda x: (x>=4),[2,4,7,1,8]))
print(list(c))

# map() func within filter() func

d = filter(lambda x: (x>=5),map(lambda x: x*2,[2,3,4,1,7]))
print(tuple(d))

# map() and filter() within reduce()

r = reduce(lambda x,y: x+y,map(lambda x: x+x, filter(lambda x: x>=4,[1,2,3,4,5,6,7])))
print(r)

