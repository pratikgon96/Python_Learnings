class student:

    school = "BMHS"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school

s1 = student(32,42,52)
s2 = student(34,53,48)
print(student.getschool())
print(s1.avg() ,s2.avg())