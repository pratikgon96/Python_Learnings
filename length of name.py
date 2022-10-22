

def count(lst):
    less_than_six = 0
    for i in lst:
        if len(i)<=6:
            print(i)
            less_than_six+=1
    return less_than_six




lst = ['pratik','priya','aniket','nabanita','raya','rajarshi','piyush','arghya']

less_than_six = count(lst)
print(less_than_six)
print(f"less_than_six: {less_than_six}")