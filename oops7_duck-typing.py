class PayCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("spelling check")
        print("convention check")
        print("Rompiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()


#ide = PayCharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)