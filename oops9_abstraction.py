from abc import ABC, abstractmethod

class Father(ABC):
    def show(self): #abstract_method
        pass
    def disp(self): #concrete_method
        print("fuck off")


class Child(Father):
    def show(self):
        print("dumb ass")
        print("mother Fucker")

c = Child()
c.show()
c.disp()