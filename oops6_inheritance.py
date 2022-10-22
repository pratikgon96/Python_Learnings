#Method_resolution_order
#constructor_in_inheritance
#super() method

class A:
    def __init__(self):
        print("a in init")
    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')

class B:
    def __init__(self):
        print("b in init")
    def feature1(self):
        print('feature1b is working')
    def feature4(self):
        print('feature4 is working')

class C(B,A):
    def __init__(self):
        super().__init__()
        print("c in init")
    def feature5(self):
        print('feature5 is working')
    def feat(self):
        super().feature2()

a1 = C()
a1.feature1()
a1.feat()
