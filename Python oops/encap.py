class MyInt(object):
    #def set_val(self,val):
     #   try:
      #      val = int(val)
       # except ValueError:
        #    return

    def __init__(self,value):
        print ("print init")
        try:
            val = int(value)
        except ValueError:
                value = 0

        self.val = value

    def get_val(self):
        return self.val

    def inc_val(self):
        self.val = self.val + 1


i = MyInt("hi")
#i.set_val()
print(i.get_val())
i.inc_val()
print(i.val)
#i.val = "hi"
#print(i.inc_val())