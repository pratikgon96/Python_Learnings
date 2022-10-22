num = [int(d) for d in input("Enter the number:")]
print(type(num))
even,odd = 0,0
for i in range(0,len(num)):
    if i % 2 ==0:
        even = even + num[i]
    else:
        odd = odd + num[i]

print(abs(odd-even))
