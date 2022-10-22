class student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.laptop()
    def show(self):
        print(self.name,self.roll_no)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.ram = 8
            self.cpu = 'i5'

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student('Pratik',37)
s2 = student('Priya',41)

s1.show()
s2.show()