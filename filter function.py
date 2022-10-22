from functools import reduce

#def is_even(n):     #(This process is done by calling a function name is_even)
#    return n%2==0

nums = [11,32,54,88,45,34,12,96,33,78]

#evens = list(filter(is_even,nums))
evens = list(filter(lambda n: n%2==0,nums))   #this process is done by calling a lambda fuction in the filter fuction itself
doubles = list(map(lambda n: n*2,evens))  #this can be done: def update(n): return n*2
sum = reduce(lambda a,b: a+b ,doubles)
print(evens)
print(doubles)
print(sum)

