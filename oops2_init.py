class computer:
    def __init__(self,processor,ram):
        self.processor = processor
        self.ram = ram

    def config(self):
        print("config is: ",self.processor,self.ram)

com1 = computer('i5',16)
com2 = computer('AMD',8)

com1.config()
com2.config()