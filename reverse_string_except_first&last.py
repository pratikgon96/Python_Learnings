#Reverse each character of a given string except the first and the last character remain in the same position.
#ex. i/p: This is a coding question of reversing a string
# o/p: Tihs is a cnidog qoitseun of rnisreveg a snirtg


s = input("Enter the string to perform: ")

n = s.split()
print(n)

for i in n:
    if len(i) > 3:
        print(i[0] + i[1:len(i)-1][::-1] + i[-1], end=" ")
    else:
        print(i,end=" ")