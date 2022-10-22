import random
moves = ['rock','paper','sci']
m_count = int(input("how many times you wanna play: "))
keep_pl = 0
win = 0
c_win = 0
while keep_pl < m_count:
    cmove = random.choice(moves)
    pmove = input("enter your choice: ")
    pmove = pmove.lower()
    print("the computer chose: ",cmove)

    if pmove == cmove:
        print("draw")
    else:
        if pmove=='rock' and cmove=='paper':
            print("you lose")
            c_win += 1
        elif pmove=='rock' and cmove=='sci':
            print("you win")
            win += 1
        elif pmove=='paper' and cmove=='sci':
            print("you lose")
            c_win += 1
        elif pmove=='paper' and cmove=='rock':
            print("you win")
            win += 1
        elif pmove=='sci' and cmove=='rock':
            print("you lose")
            c_win += 1
        elif pmove=='sci' and cmove=='paper':
            print("you win")
            win += 1
        else:
            print('fuck off!')

        keep_pl += 1
print('your score: ',win)
print('computer score: ',c_win)
if win > c_win:
    print("congratulations!you won!")
elif win < c_win:
    print('you lose dumb ass!')
else:
    print('Draw')