# Assignment1.py
# Course: IT3883/Section W01
# Student Name: Christian Scott
# Assignment Number: Lab 1
# Due Date: 09/05/2025
# Description: This program allows the user to input a string and append it to a buffer.  The user will also be able to clear the buffer and display the buffer.
# Resources used: Module 1-1 --> Input-output

# Assignment:
# Option 1: Append data to the input buffer
# This option will prompt the user for a string and append it to any previous input that has been provided.

#Option 2: Clear the input buffer
#This option will clear any data that has been previously input.

#Option 3: Display the input buffer
#This option will print to the screen whatever input data is currently being saved.

#Option 4: Exit the program
#This option will exit the program.

print("Input Buffer Program")
exit = False
input_string = ""

while exit == False:
  print(
      "\nOption 1: Append data to the input buffer. \nOption 2: Clear the input buffer. \nOption 3: Display the input buffer. \nOption 4: Exit the program.\n\nInsert an option 1-4:\n")

  option = int(input())
  print("Option Selected: " + str(option) + "\n")

  if option == 1:
    print("Input a string\n")
    input_string = input()
    print("String Appended\n")
  elif option == 2:
    input_string = ""
    print("Buffer Cleared\n")
  elif option == 3:
    print(input_string)
  elif option == 4:
    exit = True
    print("Program Exited\n")
  else:
    print("Invalid Option\n")