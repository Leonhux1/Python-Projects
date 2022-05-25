# Name = Faizan Rafieuddin.
# Name of the program = "Encoding and Decoding a file"
# Description = "This program uses a Ceaser Cipher to encode and decode
#                text from a file, which is then written to another file".

# Creating the main function.
def main():

    # Declaring and Initializing stuff.
    global codes        # Declaring the variable 'codes' as global which is going to store the cipher.

    # Filling in the global dictionary 'codes'.
    codes = {'A' : 'D', 'B' : 'E' , 'C' : 'F' , 'D' : 'G' , 'E' : 'H' , 'F' : 'I' , 'G' : 'J' , 'H' : 'K' , 'I' : 'L' , 'J' : 'M' , 'K' : 'N' , 'L' : 'O', 'M' : 'P' , 'N' : 'Q', 'O' : 'R' , 'P' : 'S' , 'Q' : 'T' , 'R' : 'U' , 'S' : 'V' , 'T' : 'W' , 'U' : 'X' , 'V' : 'Y' , 'W' : 'Z' , 'X' : 'A' , 'Y' : 'B' , 'Z' : 'C'}

    main_List = []      # Will store the contents of the file in a list.

    encrypted_List_To_Write = []    # Will store the encrypted contents of the main_List.

    decrypted_List_To_Write = []    # Will store the decrypted contents of the main_List.

    index = 0                     # Used as a target variable by one of the for loops.

    string = ''                     # Will store the elements of a list as text for writing in the console window.

    flag = True                     # Boolean variable to control the while loop.

    choice = 0                      # Will store the users choice, for encryption or decryption.

    input_User_File = ''            # Will reference the inputted value of the input file.

    output_User_File = ''           # Will reference the inputted value of the output file.

    again = ''                      # Will store the value of whether the user wants to run the program again or not.

    element = ''                    # Used as a target variable in the for loop.

    # The while loop, which will run till the flag is true.
    while flag:

        # Printing the opening message and asking the user for a choice (whether to encrypt or decrypt).
        print("Welcome to the encryption/decryption program.\nPlease press 1 for encryption or 2 for decryption.\n")
        print("1.\tEncryption\n2.\tDecryption")
        choice = int(input("\nPlease enter your choice: "))

        # If the choice is encryption, this block of code is executed.
        if (choice == 1):
            
            print()

            # Asking the user to input the file names from which the program is going to read from and write to.
            input_User_File = input("Please enter the file name (with the extension .txt) which you are going to encrypt: ")

            output_User_File = input("\nPlease enter the file name (with the extension .txt) which you are going to write to: ")

            # Opening the file for reading.
            file_For_Encryption = open(input_User_File , 'r')

            # Calling the 'file_To_List_For_Encryption()' function, that is going to convert the text read in from the file to a list.                            
            main_List = file_To_List_For_Encryption(file_For_Encryption)

            # Calling the 'encryption()' function with the attribute 'main_List'. This is going to encrypt the text with the cipher and return
            # a list of the encrypted text.
            encrypted_List_To_Write = encryption(main_List)

            # Opening the file to which we are going to write the encrypted message to.
            output_File_To_Write_Encrypted = open(output_User_File , 'w')

            # Iterating through the list above, and writing the contents of the list (encrypted file) to the 'output_File_To_Write_Encrypted' file.
            for index in range(len(encrypted_List_To_Write)):
                output_File_To_Write_Encrypted.write(encrypted_List_To_Write[index])

            # Printing out the encrypted message with appropriate formatting and a message confirming that the text has been written to the file.
            print("\nHere's your encrypted text.\n********************************************************************\n")

            for element in encrypted_List_To_Write:
                string += element

            # Closing the files.
            file_For_Encryption.close()
            output_File_To_Write_Encrypted.close()

            print(string)
            print()
            print("********************************************************************\nYour text has been successfully converted and written!")
            print()

            # Asking the user if he/she wants to run the program again.
            again = str(input("Do you want to run the program again? (Type 'yes' for running the program again or press enter to exit the program): "))

            # If the user wants to run the program again, this block of code is run, and the variables that had stored something are initialized again.
            if (again == "Yes" or again == "yes"):
                flag = True
                string = ''
                print()
            # If the user wants to exit the program, the flag is set to false and the ending message is printed.
            else:
                flag = False
                print()
                print("Thankyou, Goodbye.")

        # If the user wants to decrypt a file, this block of code is executed.
        elif (choice == 2):
            print()

            # Asking the user to input the names of the files to read from and write to.
            input_User_File = input("Please enter the file name (with the extension .txt) which you are going to decrypt: ")

            output_User_File = input("\nPlease enter the file name (with the extension .txt) which you are going to write to: ")

            # Opening the file to read the decrypted message into the program.
            file_For_Decryption = open(input_User_File, 'r')

            # Converting the decrypted message read in from the file to a list by calling the 'file_To_List_For_Decryption()' function.
            main_List = file_To_List_For_Decryption(file_For_Decryption)

            # Decrypting the converted list above by sending that list to the 'decryption()' function.
            decrypted_List_To_Write = decryption(main_List)

            # Opening the file to write to.
            output_File_To_Write_Decrypted = open(output_User_File , 'w')

            # Iterating through the decrypted list, and writing the contents of that list to a file.
            for index in range(len(decrypted_List_To_Write)):
                output_File_To_Write_Decrypted.write(decrypted_List_To_Write[index])

            # Printing out the decrypted text with appropriate formatting and a message that indicates that the message has been written to the file.
            print("Here's your decrypted text.\n********************************************************************\n")

            for element in decrypted_List_To_Write:
                string += element

            file_For_Decryption.close()
            output_File_To_Write_Decrypted.close()

            print(string)
            print()
            print("********************************************************************\nYour text has been successfully converted and written!")
            print()

            # Asking the user if he/she wants to run the program again.
            again = str(input("Do you want to run the program again? (Type 'yes' for running the program again or press enter to exit the program): "))

            # If the user wants to run the program again, this block of code will be executed
            if (again == "Yes" or again == "yes"):
                flag = True
                string = ''
                print()
            # If the user wants to exit the program, the flag is set to false, and the ending message is displayed.
            else:
                flag = False
                print()
                print("Thank you, Goodbye.")


        # If the user enters an option other that 1 or 2 (for encryption and decryption respectively), this message is shown.    
        else:
            print("Invalid Choice")


# Defining the 'encryption' function that is going to encrypt the contents of a file.
def encryption(original_List):

    # Declaring and Initializing stuff.
    number = 0          # Used as a target variable in the for loop.
    output_List = []    # Will store the encrypted message as a list.
    
    for number in range(len(original_List)):
        if (original_List[number]) == " ":
            output_List.append(" ")
        else:
            output_List.append(codes[original_List[number]])
    return output_List


# Defining the 'file_To_List_For_Encryption()' function that will convert the contents of the file into a list
def file_To_List_For_Encryption(file_Object):

    # Initializing stuff.
    decrypt_List = []       # This will store the contents read in from the file as a list.
    letter = ''             # This acts as a target variable for the for loop.
    decrypt_Text = ''       # This will store the contents of the file.

    # Reading from the file.
    decrypt_Text = file_Object.read()

    # For every letter in the string 'decrypt_Text', if the letter is an alphabet, it is added to the list, otherwise a space is added.
    for letter in decrypt_Text:
        if letter.isalpha():
            decrypt_List.append(letter.upper())
        else:
            decrypt_List.append(" ")

    # Closing the file.
    file_Object.close()

    # Returning the list to the call site.
    return decrypt_List


## The functions below this work in the same way as the functions above, except they are for files to be decrypted.

# Defining the 'file_To_List_For_Decryption()' function that will convert the contents of the file into a list.
def file_To_List_For_Decryption(file_Object1):

    # Initializing stuff.
    encrypt_Text = ''       # Will store the text read in from the file.      
    value = ''              # Will act as a target variable for the for loop.
    encrypted_List = []     # Will store the contents of the file as a list.
    
    encrypt_Text = file_Object1.read()

    for value in encrypt_Text:
        if value.isalpha():
            encrypted_List.append(value)
        else:
            encrypted_List.append(" ")

    file_Object1.close()
    return encrypted_List


def decryption(original_List1):

    # Initializing stuff.
    decrypt_List1 = []      # Will store the decrypted message from the file, as a list.
    index_Of_List = 0       # This represents the value of the index of the key_List
    value_List = []         # This stores the values of the global codes dictionary.
    key_List = []           # This stores the keys of the global codes dictonary.
    numericals = 0          # Acts as a target variable in the for loop.


    value_List = list(codes.values())
    key_List = list(codes.keys())
    
    for numericals in range(len(original_List1)):
        if (original_List1[numericals] == " "):
            decrypt_List1.append(" ")
        else:
            index_Of_List = value_List.index(original_List1[numericals])
            decoding = key_List[index_Of_List]
            decrypt_List1.append(decoding)
            
    return decrypt_List1    
    
            
    
    
# Calling the main function.
main()


        

