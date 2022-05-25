# Name = Faizan Rafieuddin.
# Program Name = "State Capital Quiz"
# Description = "This program quizzes the user on the capitals of the US states,
#                until the user decides to quit the program. All of the results
#                are shown in the end."

# Importing the random module for some of its functions.
import random

# Defining the main function.
def main():
    # Declaring and Initializing stuff.
    incorrect = 0       # Will count all of the incorrect values the user enters (accumulator).

    correct = 0         # Will count all of the correct values the user enters (accumulator).
    
    main_Dict = dict()  # Will store all the states as keys, and their respective capitals as values.
    
    flag = True         # Will control the while loop. 

    correct_List = []   # Will store all the values that the user got correct.

    incorrect_List = [] # Will store all the values that the user got wrong.

    correct_Answers = '' # Acts as a target variable for one of the for loops for iterating through the correct_Answers, for printing them.

    incorrect_Answers = '' # Acts as a target variable for one of the foor loops for iterating through the incorrect_Answers, for printing them.

    key_List = []       # Will hold all of the keys for the dictionary 'main_Dict'.

    start = ''          # Acts as a pushing variable, that prompts the program to progress on.

    rand_Num_List = []  # Will store the returned list of non-repeated numbers from 0-49, from the 'rand_Number_Generator' function.

    index = 0           # Acts as a target variable for one of the for loops and will also act as an index to the 'rand_Num_List'.

    number = 0          # Will store the values from the 'rand_Num_List'.

    state = ''          # Will store the states to be asked.

    tab = ''            # Will store the tabs (\t) according to the length of the states (used in printing the result).

    resposne = ''       # Will hold the users answers.

    again = ''          # Will store the users answer on 'whether to run the program again or not?'.

    # Executing this block of code while the flag remains true.
    while flag:
        # Calling the 'file_Reader()' function that will return the contents read from the file as a dictionary.
        main_Dict = file_Reader()

        # Converting the keys of the recieved dictionary above, to a list.
        key_List = list(main_Dict.keys())

        # Printing the welcome or the starting messages.
        print("\nWelcome to the US state and their Capitals Quiz!.\n")
        print("Now I will show the states in the US, and you are going to give their capitals as the answer")
        print("(please make sure that the first letters of the answers are Upper Case or capitalized). You")
        print("can leave the program any time you want by typing quit in the area in which you are going to")
        print("write the capitals.")
        print("***********************************************************************************************")

        # Asking the user whether he/she wants to enter the program or quit the program.
        start = input("Please press enter to start or if you want to quit the program before starting, press anything.\n")

        # If the user wants to enter the program, this block will run.
        if start == '':

            # Calling the 'random_Number_Generator' function, that returns a list of 'non repeated' random numbers from 0 to 49 (inclusive).
            rand_Num_List = random_Number_Generator(main_Dict)

            # Iterating through the list of random numbers recieved above, and using that value as an index to the list of keys of the 'main_Dict'.
            for index in range(len(rand_Num_List)):

                # Storing a number from the ran_Num_List to the 'number' variable.
                number = rand_Num_List[index]

                # Storing random states to be asked in the 'state' variable.
                state = key_List[number]

                # This if-else loop below is for spacing accordingly.
                if (len(state) >= 7):
                    tab = '\t'
                else:
                    tab = '\t\t'

                # Printing the states out.
                print(state, tab, end = '')

                # Waiting for an answer.
                response = input("Your response: ")

                # If the answer is 'quit', the program will ask the user once again for confirmation and then act accordingly.
                if (response == 'quit'):
                    # Subtracting 1 from the 'incorrect' accumulator, for the results to remain stable.
                    incorrect +- 1
                    # Breaking through the loop.
                    break

                # If the answer is correct, add one to the 'correct' accumulator, and add the state of that answer to the 'correct_Answer' list.
                if (response == main_Dict[state]):
                    correct += 1
                    correct_List.append(state)
                # Else, add 1 to the 'incorrect' accumulator, and add the state of the incorrect answer to thte 'incorrect_Answer' list.
                else:
                    incorrect += 1
                    incorrect_List.append(state)

            # Printing the required output with appropriate formatting and readability.
            print()
            print("*********************************************************************")
            print("Correct\t\t" , correct, "\n")
            print("Incorrect\t", incorrect, "\n")
            print("Total Asked\t" , correct + incorrect)
            print("(on the last question, the program ended or the user decided to quit.)")
            print("*********************************************************************")
            correct, incorrect = 0, 0
            print()

            # Printing out the heading for the correct answers.
            print("Correct Answers!")
            print("****************")
            print()

            # Printing out the correct answers.
            for correct_Answers in correct_List:
                if (len(main_Dict[correct_Answers]) >= 7):
                    tab = '\t'
                else:
                    tab = '\t\t'
                    
                print(main_Dict[correct_Answers] , tab, "   for\t\t", correct_Answers)
                print()

            # Prining out the heading for the incorrect answers and their correct answers.
            print("Incorrect Answers And Their Correct Answers")
            print("*******************************************")
            print()

            # Printing out the incorrect answers the user entered (or left blank) and their correct answers.
            for incorrect_Answers in incorrect_List:
                if (len(incorrect_Answers) >= 7):
                    tab = '\t'
                else:
                    tab = '\t\t'
 
                print(incorrect_Answers, tab,  "correct: ", main_Dict[incorrect_Answers])
                print()
            

            print()

            # Asking the user if he/she wants to play the quiz game again?
            again = input("Think Twice! do you want to exit? (Type 'no' for playing the game again, or 'quit' to exit): ")

            # If the user does not want to quit, the accumulators and the lists are initialized again.
            if (again == 'no'):
                flag = True
                correct_Answers, incorrect_Answers, incorrect_List, correct_List = [], [], [], []
            elif (again == 'No'):
                flag = True
                correct_Answers, incorrect_Answers, incorrect_List, correct_List = [], [], [], []

            # If the user wants to quit, the flag is set to 'False' to exit the while loop and the ending message is displayed.
            elif (again == 'quit'):
                flag = False
                print("\nThankyou, Goodbye.")
            else:
                flag = False
                print("\nThankyou, Goodbye.")
                
        # If the user does not press 'enter' to enter into the program, types 'quit' or presses anything else, the program ends and the ending message is displayed.
        else:
            flag = False
            print()
            print("Thankyou, Goodbye.")





# Defining the 'file_Reader()' function that is going to read the contents of the file, and convert them into mappings (key-value pairs) or a dictionary.
def file_Reader():

    # Opening the file to read.
    infile = open('state_capitals.txt', 'r')

    # Initializing stuff.
    all_Dict = dict()   # Creating a dictionary to store the contents of the file.

    capitals = ''       # Will store the capitals of the states, read in from the file.

    states = ''         # Will store the states read in from the file.

    # Reading in from the file.
    states = infile.readline().rstrip("\n")

    # Reading in from the file, till the end of the file and storing the values as key-value pairs in a dictionary.
    while states != '':
        capitals = infile.readline().rstrip("\n")
        all_Dict[states] = capitals
        states = infile.readline().rstrip("\n")

    # Closing the file.
    infile.close()

    # Returning the dictionary to the call location.
    return all_Dict

# Defining the 'random_Number_Generator()' function that is going to create and return a non-repeated range of numbers from 0-49 stored in a list.
def random_Number_Generator(dictionary):

    # Initializing stuff.
    random_List = []        # Will store the random numbers.
    numerical = 0           # Used as a target variable by the for loop.

    # Generating a list of numbers from 0-49 and storing them in 'random_List'.
    for numerical in range(0, len(dictionary)):
          random_List.append(numerical)

    # Shuffling and returning the list.
    random.shuffle(random_List)
    return random_List

# Calling the main function for the program to run.
main()
