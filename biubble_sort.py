def bubble(list):
    for i in range(len(list)-1):
        for j in range(0,len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


list = [2,5,9,1,3,4,7,8,6]
bubble(list)
print(list)