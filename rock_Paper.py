import random
from tkinter import E

choices= ['rock','paper','scissors']

computer= random.choice(choices)
player=None

while player not in choices:
    player=input('Rock,Paper or Scissors?:').lower()

    if computer==player:
        print('computer:',computer)
        print('Player:',player)
        print('This is a tie')
    else: 
        if computer=='rock':
            if player=='paper':
                print("Computer:",computer)
                print("Player:",player)
                print('player wins')
        else:
            if computer=='paper':
                if player=='rock':
                    print("Computer:",computer)
                    print("Player:",player)
                    print('computer wins')
            else:
                if computer=='scissors':
                    if player=='rock':
                        print("Computer:",computer)
                        print("Player:",player)
                        print('player wins')
                else:
                    if player=='scissors':
                        if computer=='rock':
                            print('Computer',computer)
                            print('Player',player)
                            print('Computer wins')
                    else:
                        if player=='paper':
                            if computer=='rock':
                                print('Computer',computer)
                                print('Player',player)
                                print('Player wins')
                        else:
                            if player=='paper':
                                if computer=='scissors':
                                      print('Computer',computer)
                                      print('Player',player)
                                      print('Player wins')
                    

             
