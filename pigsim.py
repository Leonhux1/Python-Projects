# Name = Faizan Rafieuddin.
# Name of the program = "Pigsim"
# Description = "This program is a strategy based program for the game "Pig".
#                This program allows two computers to compete against each
#                using different strategies, and reports back the total result
#                of the competition as well as the strategy used to play".

# Importing the random and time module for rolling the die and for halting the computer turn for making the program more realistic.
import random

import time

# This function handles the rolling of the die by the user and the computer.
def roll_die():
    # Generating a random number from 1 to 6 and returning that to the call site.
    randomnum = random.randint(1, 6)
    
    return(randomnum)

# This function handles the choice that the user makes on whether to proceed with his/her turn or not.
def user_choice():

    print()     # Leaving a blank line.

    # The choice of the user is stored in the variable 'choice'.
    choice = input("Do you want to roll the dice(type 'yes' for accepting or 'no' for declining): ")
    # If the user wants to play, a true is returned to the call site, otherwise a false is returned.
    if choice == "Yes" or choice == "YES" or choice == "yes":
        return True
    else:
        return False

# This function handles everything relating to the computers turn and also sums and returns the score of the computers turn in the end.    
def computer_take_turn():

    # Initializing the necessary variables.
    compturn = True         # This variable will control the while loop.

    total = 0               # This will accumulate all of the computers score for each turn.

    upperlimit1 = 23        # This variable is used to tell the computer to roll until the total is less than 23.

    comproll = 0            # This will store the value for each die roll this computer makes.

    # This block of code will execute repeatedly until the variable 'compturn' is true.
    while (compturn):
        # The roll of the die is stored in the variable 'comproll'.    
        comproll = roll_die()

        # If the die roll for this turn is equal to 1, the turn ends and the entire total (for that turn) is set to 0.
        if comproll == 1:
            compturn = False            # The while loop is exited i.e. the turn ends.
            total = 0

        # If the computers roll is equal to anything between 2 and 6, this block of code gets executed.
        else:
            # If the current total of this computer goes greater than or equal to 23, the while loop is exited.
            if (total + comproll) >= upperlimit1:
                total += comproll
                compturn = False
            # Else, the roll is added to the total.
            else:
                total += comproll

    return total        # The current total is returned.

# This function handles everything regarding the turn of the second computer and returns the total for the turn to the call site.
def computer2_take_turn():

    # Initializing neccesary variables.
    compturn2 = True        # This variable controls the while loop.

    total2 = 0              # The total for each turn is accumulated in this variable.

    upperlimit2 = 20        # This variable limits the computers rolls i.e. its score would always be less than 20.

    comproll = 0            # This will store the value for each roll.
    
    # This block of code gets executed repeatedly provided compturn2 remains true, otherwise the loop is exited.
    while (compturn2):
        # The die roll for this computer is stored in this variable.            
        comproll2 = roll_die()

        # If the roll for this turn equals to 1, the current total for this turn is set to 0 and the while loop is exited.
        if comproll2 == 1:
            compturn2 = False           # While loop gets exited.
            total2 = 0
        # Else, if the roll is between 2 and 6, this block gets executed.
        else:
            # If the current total is exceeding or equal to 20, the while loop is exited.
            if (total2 + comproll2) >= upperlimit2:
                total2 += comproll2
                compturn2 = False
            # Else, if the current total isn't exceeding 20, the roll gets added to the total.
            else:
                total2 += comproll2

    # The total for that turn is returned to the call site.
    return total2


# This function checks for if there is a winner between both of the computers and returns a bool accordingly.
def check_for_win(computer, computer2):

    who_Won = bool          # This stores the value for each case i.e. computer wins, computer looses, user wins, user looses etc.
    
    # If the score for computer 1 is greater than computer 2, this block gets executed.
    if (computer > computer2):
        # If computer 1's score is less than 100, there is no winner and a false is returned.
        if (computer < 100):
            who_Won = False
        # If the computer 1's score is exceeding or equal to 100, the winner is computer 1 and a true is returned.
        else:
            who_Won = True
    # If computer 2's score is greater than that of computer 1, this block of code gets executed.
    elif (computer2 > computer):
        # If computer 2's score is less than 100, there is no winner and a false is returned.
        if (computer2 < 100):
            who_Won = False
        # If computer 2's score is equal to or greater than 100, computer 2 wins the game and a true is returned to the call site.
        else:
            who_Won = True
    # If computer 2's score is equal to that of computer 1's, this block gets executed.
    elif (computer2 == computer):
        # If computer 2's score is equal to the winning requirement (that means computer 1 is also same), a true is returned to the call site.
        if (computer2 == 100):
            who_Won = True

    # Otherwise, a false is returned i.e. there is no winner.
    else:
        who_Won = False

    return who_Won          # Returns True of False depending on if a winner was found.

# The main function handles all of the turns and checks for a winner and shows the overall wins per a 1000 game serie for both of the computers.
def main():
    # Initializing the variables necessary.
    overall_Win = 0         # Will store all the wins for computer 1

    overall_Win2 = 0        # Will store all the wins for computer 2.
    
    flag_Super = True       # Is used as a control variable in the first while loop.
    
    flag2 = 0               # Is used as an accumulator to track the games played upto a 1000.

    winner = bool           # Will store the recieved value from a the function check_for_win() to check for a potential winner.

    # Printing out the heading.
    print("Testing Computer1 for 23 against Computer2 for 20:- ")
    print("****************************************************\n")

    # While flag_Super remains true, this block of code gets executed repeatedly.
    while (flag_Super):
    
        flag = True             # After each game the flag is set to true to repeat uptil a 1000 times.

        computer2_Turn = 0      # Each score for computer 2's turn is stored in this variable.

        computer2_Total = 0     # This accumulates all of the scores for computer 2.

        computer_Turn = 0       # Each score for computer 1's turn is stored in this variable.

        computer_Total = 0      # This accumulates all of the scores for computer 1.

        # This block of code gets executed repeatedly provided the variable 'flag' remains true.
        while (flag):

            # This will store the value for each turn of computer 2.
            computer2_Turn = computer2_take_turn()

            # This will accumulate the score of computer 2 throughout each game.
            computer2_Total += computer2_Turn

            # This will check for a winner.
            winner = check_for_win(computer_Total, computer2_Total)

            # If there is a winner, this block gets executed.
            if winner == True:
                flag2 += 1      # flag2 is incremented by 1.

                # If computer 1 wins, overall_Win is incremented by 1.    
                if(computer_Total > computer2_Total):
                    overall_Win += 1
                    flag = False        # Inner while loop is exited.

                # If computer 2 wins, overall_Win2 is incremented by 1.        
                elif(computer2_Total > computer_Total):
                    overall_Win2 += 1
                    flag = False        # Inner while loop is exited.

                else:
                    flag = False        # In the case of a tie, inner while loop is exited.

            # Else, the current game is still carried on.
            else:
                flag = True
                    
            # If computer 2 wins, this block is ignored.
            if not(computer2_Total >= 100):

                # Computer 1 takes its turn and the result gets stored in the variable computer_Turn.        
                computer_Turn = computer_take_turn()
                # Computer 1's score is accumulated for each game.
                computer_Total += computer_Turn

                # After each turn, a winner is checked for.
                winner = check_for_win(computer_Total, computer2_Total)

                # If there is a winner, this block gets executed. It is similar to the one above, that acts in case of a winner.
                if winner == True:
                    flag2 += 1
                        
                    if(computer2_Total > computer_Total):
                        overall_Win2 += 1
                        flag = False
        

                    elif(computer_Total > computer2_Total):
                        overall_Win += 1
                        flag = False

                    else:
                        flag = False

                # If a winner is not found, the current game continues.
                else:
                    flag = True



        # Until a 1000 games are not played, the outer while loop gets executed repeatedly.        
        if (flag2 != 1000):
            flag_Super = True

        # As soon as 1000 games are over between computer 1 and computer 2, the results are printed and the program ends.    
        else:
            print("Computer 1 total wins =", overall_Win)
            print("Computer 2 total wins =", overall_Win2)
            flag_Super = False



main()      # Main function gets called.
    

            
        

    
