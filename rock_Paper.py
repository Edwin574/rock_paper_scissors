import random
from tkinter import E

choices= ['rock','paper','scissors']

computer= random.choice(choices)
player=None

while player not in choices:
    player=input('Rock,Paper or Scissors?:').lower()
    print(computer)

    if computer==player:
        print('computer:',computer)
        print('Player:',player)
        print('This is a tie')
    elif computer=='rock':
            if player=='paper':
                print("Computer:",computer)
                print("Player:",player)
                print('player wins')
            else:
                if player=='scissors':
                    print("Computer:",computer)
                    print("Player:",player)
                    print('computer wins')
    elif computer=='paper':
        if player=='rock':
            print("Computer:",computer)
            print("Player:",player)
            print('computer wins')
        else:
            if player=='scissors':
                print('Computer',computer)
                print('Player',player)
                print('player wins')
    else:
        if player=='paper':
                
            print('Computer',computer)
            print('Player',player)
            print('computer wins')
        else: 
           if player=='rock':
            print('Computer',computer)
            print('Player',player)
            print('Player wins')
               
                    

             
