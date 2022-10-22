#there is a max value of a given list and a push method to append the data to the list. If the max value suppresed then the 1st element to be pushed will be poped.
class MaxSizeList(object):
    def __init__(self,max):
        self.max = max
        self.list = []

    def push(self,val):
        self.list.append(val)
        if(len(self.list) > self.max):
            self.list.pop(0)

    def get_list(self):
        return self.list


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('hi')
a.push('fuck')
a.push("mother")
a.push("chod")
a.push('simon')

b.push(4)
b.push(9)

print(b.get_list())
print(a.get_list())