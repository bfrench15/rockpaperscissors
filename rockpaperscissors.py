#import needed modules
import random
import time

#welcome user
name = input("\nWhat is your name? ")
print ("Hello, " + name, "let's play ROCK, PAPER, SCISSORS! \n")
time.sleep(3)

#print game instructions
print('Rules for winning ROCK, PAPER, SCISSORS are: \n'
      + "Rock beats Scissors \n"
      + "Scissors beats Paper \n"
      + "Paper beats Rock \n")

while True:
    print ("\nChoose you fighter: \n 1 = rock \n 2 = paper \n 3 = scissors \n")
    
    #take user input for selection
    choice = int(input("Enter your choice: "))
    
    #loop until invalid input
    while choice > 3 or choice < 1:
        choice = int(input("Error! Please enter a valid option."))
        
    #initialize values of choice.name variable to correspond with values
    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissors'
        
    #print selection
    print("\nYou chose ", choice_name)
    time.sleep(1)
    print('Now its my turn...')
    time.sleep(1)
    
    #random module used for computer to select randomly 1, 2, or 3
    compchoice = random.randint(1,3) 
    
    #loop until compchoice value is equal to choice value
    while compchoice == choice:
        compchoice = random.randint(1,3)
        
    #initialize value og compchoice.name
    if compchoice == 1:
        compchoice_name = 'rock'
    elif compchoice == 2:
        compchoice_name = 'paper'
    else:
        compchoice_name = 'scissors'
    
    #print computers choice
    print("Computer's choice is " + compchoice_name)
    time.sleep(0.5)
    print(choice_name, 'vs', compchoice_name)
    
    #check to see if the game is a draw
    if choice == compchoice:
        print('Its a draw.', end = "")
        result = "DRAW"
    
    #set conditions for winning
    if (choice == 1 and compchoice == 2):
        print('paper wins \n', end = "")
        result = 'paper'
    elif (choice == 2 and compchoice == 1):
        print ('paper wins \n', end = "")
        result = 'paper'
        
    if (choice == 1 and compchoice ==3):
        print('rock wins \n', end = "")
        result = 'rock'
    elif (choice == 3 and compchoice == 1):
        print('rock wins \n', end = "")
        result = 'rock'
    
    if (choice == 2 and compchoice == 3):
        print('scissors wins \n', end = "")
        result = 'scissors'
    elif (choice == 3 and compchoice ==2):
        print('scissors wins \n', end = "")
        result = 'scissors'
    
    #print the winners name or draw if a tie
    if result == 'DRAW':
        print("Its a tie.\n")
    if result == choice_name:
        print(name, "is the ROCK, PAPER, SCISSORS champion!\n")
    else:
        print("Computer is the the ROCK, PAPER, SCISSORS champion!\n")
    
    #ask if user would like to play again
    time.sleep(2)
    print("Do you want a rematch? (Y/N) \n")
    ans = input().lower
    if ans == 'n':
        break
        print("Thanks for playing!")