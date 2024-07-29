# 2. User Input Data Processor

# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

# NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

def check_length_of_name(first_name=input("Enter first Name: "), last_name=input("Enter last name: ")):
    if len(first_name) < 2:
        raise Exception("ERROR First name should be more than 2 characters")
    elif len(last_name) < 2:
        raise Exception("ERROR Last name should be more than 2 characters")
    else:
        print(first_name + " " + last_name)

check_length_of_name()