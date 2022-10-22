n = int(input("enter the no of rows: "))

for rows in range(n):
    for cols in range(n):
        if cols == 0 or rows == (n-1) or rows == cols:
            print("*", end="")
        else:
            print(end=" ")

    print()
