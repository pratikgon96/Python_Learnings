def count(lts):
    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd



lst = [22,13,21,44,24,54,33,97,13,29,36,74,87]

even, odd = count(lst)
print(even)
print(odd)

print("Even: {} and : {}".format(even,odd))