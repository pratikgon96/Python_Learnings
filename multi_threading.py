from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello",current_thread())
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
ob1 = Hello()
ob2 = Hi()

ob1.start()
sleep(0.2)
ob2.start()

ob1.join()
ob2.join()

print("bye bye",current_thread())