def update(lst):

    print(id(lst))

    lst[1] = 23
    print('x',lst)

lst = [10,44,21]
print(id(lst))
update(lst)
print("lst",lst)