a = int(input("enter first value: "))
b = int(input("enter second value: "))

try:
    print("open the process")
    print(a/b)

    c = int(input("enter random value: "))
    print(c)
except ZeroDivisionError as e:
    print('cannot divide by zero!',e)

except ValueError as e:
    print('wrong input!')

except Exception as e:
    print('something went wrong!',e)

finally:
    print("close the process")