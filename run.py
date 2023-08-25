import gspread
from google.oauth2.service_account import Credentials
import os   # To use for clear screen
import time
import pandas as pd
import numpy as np
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)   # To initialize the colorama library
"""
To import the entire gspread library so we access any class
function or method within it.
Import credentials class which is part of the service account
function from the google oauth library.
"""
#  List the API that the program should access in order to run
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# To access 'tourism_survey' sheet, name must be same as sheet.
SHEET = GSPREAD_CLIENT.open('tourism_survey')


RED = Fore.RED      # Red color text
YELLOW = Fore.YELLOW    # Yellow color text
BLUE = Fore.BLUE    # Blue color text
RESET = Style.RESET_ALL     # Resets all the color to default
BRIGHT = Style.BRIGHT       # Text bright

# To access the data in the worksheet, parameter name same as sheet name.
text = SHEET.worksheet('text')
q_and_a = SHEET.worksheet('q_and_a')
survey_answer = SHEET.worksheet('survey_answer')
# To pull all values from the sheet.
data = text.get_all_values()
data2 = q_and_a.get_all_values()
data3 = survey_answer.get_all_values()
# print(data)
# print()
# print(data2)
# print()
# print(data3)
# print()


def clear_scr():
    """
    This function is for clear screen for different OS
    Call the clear_scr funtion to clear the terminal
    """    
    os.system('cls' if os.name == 'nt' else 'clear')


# Global variable for result
user_choice = []


def age_group():
    """
    First question in the survey
    """
    print('Q1. What is your age?')
    age_choice = ['10-18', '19-30', '31-45', '46-60', '61 and Above']
    # This is to print index number start with 1 in the choice
    for index, age_range in enumerate(age_choice, start=1):
        print(f"{index}. {age_range}")    
    print()
    user_input = 0
    while user_input < 1 or user_input > len(age_choice):
        try:
            user_input = int(input("Enter your choice: "))
            if user_input >= 1 and user_input <= len(age_choice):
                # As index always start with 0
                # user_input-1 is to get the correct number in index
                selected_age_range = age_choice[user_input-1]
                print()
                print(f"You have selected: {selected_age_range}")
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print("Please Enter a Valid Number.")
    print()
    # This is to go to function gender() next
    gender()


def gender():
    """
    Second question in the survey
    """
    print('Q2. What is your gender?')
    gender_choice = ['Male', 'Female']
    # This is to print index number start with 1 in the choice
    for index, gender_range in enumerate(gender_choice, start=1):
        print(f"{index}. {gender_range}")    
    print()
    user_input = 0
    while user_input < 1 or user_input > len(gender_choice):
        try:
            user_input = int(input("Enter your choice: "))
            if user_input >= 1 and user_input <= len(gender_choice):
                # As index always start with 0
                # user_input-1 is to get the correct number in index
                selected_gender = gender_choice[user_input-1]
                print()
                print(f"You have selected: {selected_gender}")
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print("Please Enter a Valid Number.")
    print()
    # This is to go to function continents() next
    continents()


def continents():
    """
    Third question in the survey
    """
    print('Q3. Which continent are you from?')
    continent_choice = ['Asia', 'Africa', 'North America', 'South America', 'Antartica', 'Europe', 'Australia']
    # This is to print index number start with 1 in the choice
    for index, continent_range in enumerate(continent_choice, start=1):
        print(f"{index}. {continent_range}")    
    print()
    user_input = 0
    while user_input < 1 or user_input > len(continent_choice):
        try:
            user_input = int(input("Enter your choice: "))
            if user_input >= 1 and user_input <= len(continent_choice):
                # As index always start with 0
                # user_input-1 is to get the correct number in index
                selected_continent = continent_choice[user_input-1]
                print()
                print(f"You have selected: {selected_continent}")
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print("Please Enter a Valid Number.")
    print()
    # This is to go to function destination_prefer() next
    destination_prefer()


def destination_prefer():
    """
    Fourth question in the survey
    """
    print('Q4. What type of destination do you prefer?')
    destination_choice = ['Beach', 'Culture', 'Mountain', 'Suburban', 'Urban']
    # This is to print index number start with 1 in the choice
    for index, destination_range in enumerate(destination_choice, start=1):
        print(f"{index}. {destination_range}")    
    print()
    user_input = 0
    while user_input < 1 or user_input > len(destination_choice):
        try:
            user_input = int(input("Enter your choice: "))
            if user_input >= 1 and user_input <= len(destination_choice):
                # As index always start with 0
                # user_input-1 is to get the correct number in index
                selected_destination = destination_choice[user_input-1]
                print()
                print(f"You have selected: {selected_destination}")
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print("Please Enter a Valid Number.")
    print()
    # This is to go to function planning() next
    planning()


def planning():
    """
    Fifth question in the survey
    """
    print('Q5. How do you plan your trip?')
    print()
    planning_choice = ['Through Agencies', 'Recommendations', 'Online']
    # This is to print index number start with 1 in the choice
    for index, planning_range in enumerate(planning_choice, start=1):
        print(f"{index}. {planning_range}")    
    print()
    user_input = 0
    while user_input < 1 or user_input > len(planning_choice):
        try:
            user_input = int(input("Enter your choice: "))
            if user_input >= 1 and user_input <= len(planning_choice):
                # As index always start with 0
                # user_input-1 is to get the correct number in index
                selected_planning = planning_choice[user_input-1]
                print(f"You have selected: {selected_planning}")
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print("Please Enter a Valid Number.")
    print()
    # This is to go to function motivations() next
    motivations()


def motivations():
    """
    Sixth question in the survey
    """
    print('Q6. What is the motivations for travel?')
    print()
    motivations_choice = ['Cultural', 'Foods', 'Relaxation', 'Price',
    'Shopping', 'All of the above']
    # This is to print index number start with 1 in the choice
    for index, motivations_range in enumerate(motivations_choice, start=1):
        print(f"{index}. {motivations_range}")    
    print()
    user_input = 0
    while user_input < 1 or user_input > len(motivations_choice):
        try:
            user_input = int(input("Enter your choice: "))
            if user_input >= 1 and user_input <= len(motivations_choice):
                # As index always start with 0
                # user_input-1 is to get the correct number in index
                selected_motivations = motivations_choice[user_input-1]
                print(f"You have selected: {selected_motivations}")
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print("Please Enter a Valid Number.")
    print()
    # This is to go to function influences_decision() next
    influences_decision()


def influences_decision():
    """
    Seventh question in the survey
    """
    print('Q7. What influences yourdeision making?')
    print()
    # Choice is for choice of answer
    choice = ['Clean and Tidiness', 'Price',
    'Online Review', 'Safe and Security', 'Travel Blog', 'All of the Above']
    #This is to print index number start with 1 in the choice
    for index, range in enumerate(choice, start=1):
        print(f'{index}.{range}')
    print()
    user_input = 0
    while user_input < 1 or user_input > len(choice):
        try:
            user_input = int(input('Enter your choice: '))
            if user_input >= 1 and user_input <= len(choice):
                # As index always start with 0
                # user_input - 1 is to get the correct number in index
                # Selected is for selected influences decision
                selected = choice[user_input - 1]
                print(f'You have selected: {selected}')
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    end()2
    


def update_survey_answer(age, gender, continent):
    """
    This is to update the user's answer into the sheet survey_answer
    """
    print('Updating result, please wait...\n')
    answer = [age, gender, continent]
    SHEET.worksheet('survey_answer').append_row(answer)
    print('The result updated.\n')


def submit_option(options):
    """
    Display option for user to submit the survey.
    """
    print('Thank you for completing the survey\n\n'.upper())
    print
    print('1. Submit\n'.upper())
    print('2. Exit\n'.upper())

    user_input = 0
    while user_input != 1 and user_input != 2:
        try:
            user_input = int(input('Please enter your choice: '))
            if user_input != 1 and user_input != 2:
                print('Invalid Number!')
                print('Please enter number 1 or 2')
        except ValueError:
            print('Invalid Input!')
    if user_input == 1:
        end()
    elif user_input == 2:
        exit()


def main_page():
    """
    This function allow user to choose whether to take the survey
    """
    select = 0
    while select != 1 and select != 2:
        try:
            print('Select an option: ')
            print('1. Take the survey')
            print('2. No and Exit')
            print()
            select = int(input('Please enter your choice: '))
            print()

            if select != 1 and select != 2:
                print('Invalid Number!')
        except ValueError:
            print('Please enter a valid number 1 or 2')
    if select == 1:
        clear_scr()
        age_group()
    elif select == 2:
        exit()


def welcome():
    """
    Welcome message before start the survey.
    """
    welcome_text = SHEET.worksheet('text').col_values(1)
    instruction = SHEET.worksheet('text').col_values(2)
    print()
    print(welcome_text[1])
    print()
    print()
    print(Fore.CYAN + 'System loading...' + RESET)
    time.sleep(3)
    print()
    clear_scr()
    print()
    print(RED + instruction[1].upper() + RESET)
    print()
    print(instruction[2].upper())
    print()
    input(Fore.CYAN + 'Press enter to continue...' + RESET)
    print()
    # clear_scr()
    main_page()


def end():
    """
    Ask user if they want to exit or not.
    End of survey.
    """
    select = 0
    while select != 1 and select != 2:
        try:
            print('Are you sure you want to exit?\n')
            print('1. Yes')
            print('2. No')
            select = int(input('Enter your choice: '))
            if select != 1 and select != 2:
                print('Invalid number! Please enter 1 or 2')
        except ValueError:
            print('Please enter a valid number.')

    if select == 1:
        """
        Retrieve message from sheet 'text' the third column
        """
        goodbye_msg = SHEET.worksheet('text').col_values(3)
        print(BLUE + goodbye_msg[1].upper() + RESET)
        time.sleep(3)
        exit()
    elif select == 2:
        main_page()


welcome()