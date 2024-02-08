# !/usr/bin/env python3
# Author Id: Rvanniyasingam
# A function that takes an input from the user and calculate someone’s age

from datetime import datetime

def calculate_age():
    birth_year = int(input("Please enter your Year of Birth: "))
    current_year = datetime.now().year
    age = current_year - birth_year
    print(f"You are {age} years old.")

calculate_age()
