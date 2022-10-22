import random

n = 20
to_be_guessed = int(n * random.random()) + 1 #line to generate a random number in between 20 as n is assigned 20 here.

guess = 0
count = 3
while guess != to_be_guessed:
    while count > 0:

        guess = int(input("next number: "))
        count = count - 1
        if guess > 0:
            if guess > to_be_guessed:
                print("larger number!")
            elif guess < to_be_guessed:
                print("smaller number!")
        else:
            print("sorry you are out of this game!")
            exit()
    else:
        print("out of chances!")
        break
else:
    print("congratulation! you have done it!")

