from array import *

vals = array('i',[5,7,9,-8,4,2])

newArr = array(vals.typecode,(a for a in vals))
#for i in range(len(vals)):
for e in newArr:
    #print(vals[i])
    print(e)