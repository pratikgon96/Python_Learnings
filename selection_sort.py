def selection(num, count):

    for i in range(count-1):
        print(i)
        midpos = i
        for j in range(i+1, count):
            if num[j] < num[midpos]:
                midpos = j

        if midpos != i:
            num[i], num[midpos] = num[midpos], num[i]
            print(num)


num = []
count = int(input("enter the no of elements for the list: "))
for x in range(count):
    value = int(input('enter the %d th elements of the list: '))
    num.append(value)

selection(num,count)
#print(num)