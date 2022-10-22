class person:
    def __init__(self):
        self.name = 'Pratik'
        self.age = 24

    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = person()
c2 = person()
#c1.name = 'Priya'
c1.age = 23
if c1.compare(c2):
    print("same")
else:
    print("differant")
c1.update()

print(c1.name)
print(c2.name)