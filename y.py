n = int(input())

list = []
i = 0
while i < n:
    ip = int(input())
    list.append(ip)
    i = i+1
list.sort()
l = list[len(list)-1]
list.pop(len(list)-1)
for i in range(len(list)-1,0,-1):
    if list[i] == l:
        list.remove(list[i])
    else:
        break
print(list[len(list)-1])
#l = max(list)
#while max(list) == l:
#    list.remove(max(list))
#print(max(list))