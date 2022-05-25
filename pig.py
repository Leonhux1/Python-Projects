# Name = Faizan Rafieuddin.
# Name of the Program = "Pig".
# Description = "This program is a computer vs human version of the classical "Pig"
#                game where both of the players take turns and roll dice until one
#                of the player gets a 1 (in which his/her turn gets cancelled)
#                or one of the player reaches 100 (in which that respective player
#                wins the game).

# Importing the random and time modules for rolling die and for halting the computer turn for some seconds respectively.
import random

import time

# This function is called when the user presses the button for the instructions at the beginning of the game.
def instructions():

    print()
    print("**********************************************************************************************************************")
    print()
    print("Pig is a game that has two players that alternate turns rolling dice. In our case, there will be one human player and")
    print("one computer player. Each player’s goal is to get 100 points rolled on a normal six-sided die first. Each turn consists")
    print("of the rolling the die repeatedly until you decide to stop or until you roll a 1.")
    print()
    print("For each roll:\n• If you roll a 2, 3, 4, 5, or 6 –you will add the amount rolled to your score.")
    print("• If you roll a 1 – your turn ends and you receive zero points for that entire turn (You will keep")
    print("  whatever points you had before your turn started)")
    print("• If you decide to stop rolling at any point in your turn, your points for that turn are then added to")
    print("  the overall score. The overall score is then safe from future rolls.")
    print()
    print("The key to winning pig is knowing how long to roll before deciding to stop and save your turn’s points.")
    print()
    print("***********************************************************************************************************************")
    print()

# This function is called for rolling the die, upon calling this function, a random number from 1 to 6 is returned to the call site.
def roll_die():

    randomnum = random.randint(1, 6)
    
    return(randomnum)

# This function is called for each turn the user takes for asking him/her for if he/she wants to roll the die, and then acts accordingly.
def user_choice():

    print()
    choice = input("Do you want to roll the die(type 'yes' for accepting or press enter for declining): ")

    # If the user enters 'yes', true is returned (user gets his/her turn), otherwise users turn is skipped.
    if choice == "Yes" or choice == "YES" or choice == "yes":
        return True
    else:
        return False

# This function is executed when it is the computers turn, this function entirely handles the computers turn and sums up the numbers for each turn.
def computer_take_turn():

    # Initializing necessary variables.
    compturn = True         # Used for controlling the while loop

    total = 0               # Used as an accumulator for totaling the rolls for each computer turn.

    upperlimit1 = 20        # A variable used for limiting the computers total for each turn.

    # While compturn remains true, this block will run repeatedly.
    while (compturn):

        time.sleep(0.5)         # Making the computer delay execution for more realistic gameplay.

        # Calling the roll_die() function that is going to return a value between 1 and 6 and printing it.    
        comproll = roll_die()
        print("Computer rolls-----", end = '')
        print(comproll, end = '')

        # If the value of the rolled die is 1, the while loop is exitted and all points are lost for that turn.
        if comproll == 1:
            print("-----Turn Ends!")
            compturn = False
            total = 0
        # If the value of the rolled die is between 2 and 6 (inclusive) and the total is currently less than 20, the value of the rolled die
        # is added to the total. Else, if the value of the total is greater than 20 (upperlimit1), the turn finishes.
        else:
            print()
            if (total + comproll) >= upperlimit1:
                total += comproll
                compturn = False
            else:
                total += comproll

    return total    # Returning the total at the end of each turn.


# This function is executed when it is the users turn. This function handles everything regarding the users turn and also sums up the score in the end.
def human_take_turn():

    # Initializing the variables to be used in the function.
    play = True         # Used as a control variable for the while loop.

    sumup = 0           # Used to sum up all the values of the rolls done by the user.

    humroll = 0         # Will store the value for each roll done by the user (stores a value from a function call).

    humturn = ''        # Will store the users choice for each turn (whether he/she wants to roll of not. Stores a value from a function call).


    # While the variable 'play' remains true, this block of code gets executed repeatedly.
    while (play):

        humturn = user_choice()             # The users choice on whether he/she wants to roll the die or not is stored in this variable.

        # If the user wants to roll, this block of code gets executed.
        if humturn == True:
            humroll = roll_die()            # The value for the die roll is stored in this variable.
            print()
            print("You rolled a-----", end = '')
            print(humroll, end = '')

            # If the user rolls a 1 (one), his/her turn ends and the while loop is exitted.
            if humroll == 1:
                print("-----Turn Ends!")
                sumup = 0
                play = False
            # If the user rolls a number between 2 and 6, his number gets added to his/her current total.
            else:
                print()
                sumup += humroll
                    
                
        # If the user doesn't want to roll the die, this block gets executed and the while loop is exitted.
        else:
            play = False

    return(sumup)       # Returning the total of the user at the end of his/her turn.

# This block of code checks for a winner by comparing the current scores of the computer and the user by 100.
def check_for_win(computer, user):

    who_Won = bool      # This will store the value for each result case of whether the computer wins or the user.
    
    # If computers score is greater than the user, this block gets executed.
    if (computer > user):
        if (computer < 100):    # If computers score is less than 100, a false is returned i.e. the game will still be played.
            who_Won = False
        else:                   # Else, a true is returned, that means that the computer won the game.
            who_Won = True
    # If the users score is greater than that of the computer, this block of code gets executed.
    elif (user > computer):
        if (user < 100):        # If the users score is less than 100, a false is returned i.e. the game will still proceed.
            who_Won = False
        else:                   # Else, a true is returned, that means that the user won the game.
            who_Won = True
    # If the users score is equal to the computers score, this block of code gets executed.
    elif (user == computer):
        if (user == 100):       # If the users score is equal to a 100, a true is returned.
            who_Won = True
        else:                   # Else, a false is returned, meaning the game will still proceed.
            who_Won = False        
    # Else, a false is returned.
    else:
        who_Won = False

    return who_Won          # The bool value in variable 'who_Won' is returned to the call site.

# Defining the main function that will control all of the turns and compare the results as well as print the output.
def main():

    # Initializing all of the variables to be used in the program.
    human_Total = 0         # Is used as an accumulator for each turn of the user.

    human_Turn = 0          # Will store the value for each turn of the user (stores a value from a function call).
    
    computer_Total = 0      # Is used as an accumulator for each turn of the computer.

    computer_Turn = 0       # Will store the value for each turn of the computer (stores a value from a function call).
    
    flag = True             # Is used as a control variable for the while loop in the function.

    start = 0               # Will store the users response on whether he/she would like to start the game or see the instructions or quit the game.

    winner = bool           # Will store the recieved value from a the function check_for_win() to check for a potential winner.

    # A welcome message and some choices are printed.
    print("Welcome to the python pig game program!")
    print()
    start = int(input("1.Press 1 to start the game.\n\n2.Press 2 for the instructions for this game.\n\n3.Press 3 for exiting. "))

    # While the flag remains true, this block of code gets executed repeatedly.
    while(flag):

        # If the user entered a 1 in the prompt before this, this block of code gets executed.
        if start == 1:

                # The value of the users turn is stored in the variable human_Turn and then added to the accumulator human_Total.
                human_Turn = human_take_turn()

                human_Total += human_Turn

                # At the end of each turn, the scores are printed.
                print()
                print("Your total for this turn is:", human_Turn, end = '')
                print("\t\t\tYour running total:", human_Total)
                print("****************************************************************************")
                print()

                # At the end of each turn, the check_for_win function is called with the values of the computer_Total and human_Total in parameters
                # and the result from the function call is stored in the variable 'winner'.
                winner = check_for_win(computer_Total, human_Total)

                # If there is a winner, this block of code gets executed.
                if winner == True:

                    # If the user wins, print the ending message accordingly and exit the while loop.
                    if (human_Total > computer_Total):
                        print("You won the game!", "\U0001F600")
                        flag = False
                    # If the computer wins, print the ending message accordingly and exit the while loop.    
                    elif (computer_Total > human_Total):
                        print("The computer won. You lost", "\U0001F611")
                        flag = False
                    # Else, if the scores of the computer and the user are the same, print a message saying "you tied" and exit the while loop.    
                    else:
                        print("You tied with the computer.")
                        flag = False
                        
                    
                # If a winner is not found, continue the game.
                else:
                    flag = True

                # If the user hasn't won the game, let the computer take its turn.
                if not(human_Total >= 100):
                    
                    # The value of the computers turn is stored in the variable computer_Turn (from a function call).
                    computer_Turn = computer_take_turn()

                    computer_Total += computer_Turn

                    # The output of the computers turn is printed after its each turn.
                    print()
                    print("Computers total for this turn is:", computer_Turn, end = '')
                    print("\t\tComputers running total:", computer_Total)
                    print("****************************************************************************")

                    # A winner is checked for after each turn.
                    winner = check_for_win(computer_Total, human_Total)

                    # This block of code is similar to the one above and this executes when a winner is found.
                    if winner == True:
                        print()
                        if (human_Total > computer_Total):
                            print("You won the game!", "\U0001F600")
                            flag = False
                            
                        elif (computer_Total > human_Total):
                            print("The computer won. You lost", "\U0001F611")
                            flag = False
                            
                        else:
                            print("You tied with the computer.")
                            flag = False
                            
                        
                    # If a winner is not found, the game proceeds.
                    else:
                        flag = True

        # If the user wants to see the instructions for the game i.e. if he typed 2 in the start, the instructions are shown to him/her
        # and the very first input prompt is shown again.
        elif (start == 2):
            instructions()
            start = int(input("1.Press 1 to start the game.\n\n2.Press 2 for the instructions for this game.\n\n3.Press 3 for exiting. "))

        # If the user enters a 3 in the start, exit a program.
        elif (start == 3):
            flag = False

        # If the user enters something unsual in the first input prompt, this code handle it.
        else:
            print()
            start = int(input("Incorrect choice. Either press 1 or 2: "))

    print("\nThankyou! Goodbye.")           # Printing the ending message in the end.
    
main()          # Calling the main function.
    

            
        

    
