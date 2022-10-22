class Joe(object):
    def callme(self):
        print("call me now, you mothafucker!")
        print(self)

this_obj = Joe()
this_obj.callme()
#print(this_obj.callme())

import random
class MyClass(object):
    def doIt(self):
        self.rand_val = random.randint(1,10)
        #print(self.rand_val)
my_inst = MyClass()
my_inst.doIt()
print(my_inst.rand_val)


class YourClass(object):
    classy = "hi there!"

i = YourClass()
print(i.classy)

i.classy = "fuck off!"
print(i.classy)

del i.classy
print(i.classy)