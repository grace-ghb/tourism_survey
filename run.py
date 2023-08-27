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
text = SHEET.worksheet('text').get_all_values()
q_and_a = SHEET.worksheet('q_and_a').get_all_values()
survey_answer = SHEET.worksheet('survey_answer').get_all_values()
# To pull all values from the sheet.
# data = text.get_all_values()
# data2 = q_and_a.get_all_values()
# data3 = survey_ans.get_all_values()
# print(text)
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
user_choice = ['', '', '', '', '', '', '', '', '', '', '']


def age_group():
    """
    Question 1 from sheet q_and_a
    """
    print('Q1. What is your age?')
    print()
    # Choice is for choice of answer
    choice = ['10-18', '19-30', '31-45', '46-60', '61 and Above']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is to updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function gender() next
    gender()


def gender():
    """
    Question 2 from sheet q_and_a
    """
    print('Q2. What is your gender?')
    print()
    # Choice is for choice of answer
    choice = ['Male', 'Female']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function continents() next
    continents()


def continents():
    """
    Question 3 from sheet q_and_a
    """
    print('Q3. Which continent are you from?')
    print()
    # Choice is for choice of answer
    choice = ['Asia', 'Africa', 'North America', 'South America', 'Antartica', 'Europe', 'Australia']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function destination() next
    destination()


def destination():
    """
    Question 4 from sheet q_and_a
    """
    print('Q4. What type of destination do you prefer?')
    print()
    # Choice is for choice of answer
    choice = ['Beach', 'Culture', 'Mountain', 'Suburban', 'Urban']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)    
    # This is to go to function planning() next
    planning()


def planning():
    """
    Question 5 from sheet q_and_a
    """
    print('Q5. How do you plan your trip?')
    print()
    # Choice is for choice of answer
    choice = ['Through Agencies', 'Recommendations', 'Online']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function motivations() next
    motivations()


def motivations():
    """
    Question 6 from sheet q_and_a
    """
    print('Q6. What is the motivations for travel?')
    print()
    # Choice is for choice of answer
    choice = ['Cultural', 'Foods', 'Relaxation', 'Price', 
    'Shopping', 'All of the above']
    # This is to print index number start with 1 in the choice
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function decision() next
    decision()


def decision():
    """
    Question 7 from sheet q_and_a
    """
    print('Q7. What influences your deision making?')
    print()
    # Choice is for choice of answer
    choice = ['Clean and Tidiness', 'Price',
    'Online Review', 'Safe and Security', 'Travel Blog', 'All of the Above']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function accommodation() next
    accommodation()


def accommodation():
    """
    Question 8 from sheet q_and_a
    """
    print('Q8. What type of accommodation do you prefer?')
    print()
    # Choice is for choice of answer
    choice = ['Bed and Breakfast', 'Hotels',
    'Hostel', 'Resort', 'All of the Above']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function spending() next
    spending()


def spending():
    """
    Question 9 from sheet q_and_a
    """
    print('Q9. What are you more likely to spend on during your trip?')
    print()
    # Choice is for choice of answer
    choice = ['Experiences', 'Foods', 'Shopping', 'All of the Above']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function continents() next
    experiences()


def experiences():
    """
    Question 10 from sheet q_and_a
    """
    print('Q10. How likely will you share your experiences on social media?')
    print('     Choose from 1 for unlikely to 5 very likely')
    print()
    # Choice is for choice of answer
    choice = ['1', '2', '3', '4', '5']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    # This is to go to function continents() next
    return_holiday()


def return_holiday():
    """
    Question 11 from sheet q_and_a
    """
    print('Q11. How likely would you like to come back for a holiday?')
    print('     Choose from 1 for unlikely to 5 very likely')
    print()
    # Choice is for choice of answer
    choice = ['1', '2', '3', '4', '5']
    # This is to print index number start with 1 in the choice
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
                # Update the user's andswer in the list
                user_choice[0] = selected
            else:
                print()
                print('Invalid input! Please try again.')
                print()
        except ValueError:
            print('Please Enter a Valid Number.')
    print()
    # This is updated the user choice to survey answer sheet
    update_survey_answer(user_choice)
    submit_option(user_choice)


def update_survey_answer(user_choice):
    """
    This is to update the user's answer into the sheet survey_answer
    """
    print('Updating result, please wait...\n')
    survey_answer = SHEET.worksheet("survey_answer")
    survey_answer.append_row(user_choice)
    print('The result updated.\n')


def submit_option(user_choice):
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
        print('You choose to Submit the survey.')
        time.sleep(3)
    elif user_input == 2:
        exit()


def main_page():
    """
    This function allow user to choose whether to take the survey
    """
    print('Select an option: ')
    print('1. Take the survey')
    print('2. No and Exit')
    print()
    select = int(input('Please enter your choice: '))
    print()
    if select == 1:
        clear_scr()
        age_group()
        print()
    elif select < 1 or select > 2:
        print('Invalid Input! Please Try Again.')
        print()
        main_page()
    else:
        print('You Choose To EXIT. Thank You Very Much.')
        print()


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