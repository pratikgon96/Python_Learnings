import time

sec = int(input("how much time?: "))

for i in range(sec):
    print(str(sec - i) + ' seconds remaining')

    time.sleep(1)

print("times up!")