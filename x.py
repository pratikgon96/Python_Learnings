n = int(input())
list = []

for i in range(0, n):
    a = input()
    list.append(a)
print(list)

j = 0
while j < len(list):
    k = j + 1
    while k < len(list):
        if list[j] == list[k]:
            list.pop(k)
        else:
            pass
        k = k + 1

    j = j + 1

print(list)