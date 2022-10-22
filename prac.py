#Create two stacks and from a alphanumeric string put the integers into one stack and characters to trhe other. if there is any float value in the given string then show Invalid.
#After creating the stacks pop the values and print in as the sequence given
#input: Abc12mn987z
#output: Abcmnz / 12987
#input: abt1.5cz  o/p: invalid


def createTwoStack(strValue):
    stack1 = []
    stack2 = []
    str = ""
    str1 = ""
    for i in range(len(strValue)):
        if(strValue[i].isdigit()):
            stack1.append(strValue[i])
        elif((strValue[i] >= 'A' and strValue[i] <= 'Z') or (strValue[i] >= 'a' and strValue[i] <= 'z')):
            stack2.append(strValue[i])
        else:
            print("Invalid Input")
            exit()
    for j in range(len(stack1)):
        x = stack1.pop()
        str = str + x
    print(str [::-1])
    for k in range(len(stack2)):
        y = stack2.pop()
        str1 = str1 + y
    print(str1 [::-1])

strValue = input("enter the alpha numeric string: ")
createTwoStack(strValue)
