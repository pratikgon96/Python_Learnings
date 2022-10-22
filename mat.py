from numpy import *
arr1 = array([
            [1,2,3,9],
            [4,5,6,8]

            ])

m = matrix('1 2 3; 6 4 5; 9 7 8')
m1 = matrix('6 8 7; 1 4 5; 2 3 9')
m3 = m1*m
print(m3)
print(m)
print(m.diagonal())
print(m.max())