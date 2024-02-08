# !/usr/bin/env python3
# Author Id: Rvanniyasingam
# A function that takes an input from the user and calculate someone’s age

from datetime import datetime

def calculate_age():
    try:
        birth_year = int(input("Please enter your Year of Birth: "))
    except TypeError:
        print("Please enter an int.")
        return

    current_year = datetime.now().year
    age = current_year - birth_year
    print(f"You are {age} years old.")


# Add NEW function
def helloWorld():
	print(‘Hello World’)


# Call the functions
calculate_age()

helloWorld()
