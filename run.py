import gspread
from google.oauth2.service_account import Credentials
import os   # To use for clear screen
import time
import pandas as pd
import numpy as
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
# To access 'tourism_survey' sheet, name must be same as given.
SHEET = GSPREAD_CLIENT.open('tourism_survey')


RED = Fore.RED      # Red color text
YELLOW = Fore.YELLOW    # Yellow color text
BLUE = Fore.BLUE    # Blue color text
RESET = Style.RESET_ALL     # Resets all the color to default
BRIGHT = Style.BRIGHT       # Text bright

# To access the data in the worksheet, parameter name same as sheet name.
text = SHEET.worksheet('text')

# To pull all values from the sheet.
data = text.get_all_values()


def clear_scr():
    """
    This function is for clear screen for different OS
    """
    # Call the clear_scr funtion to clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


clear_scr()


# if os.name == "posix":
#     _ = os.system("clear")
# else:
#  _ = os.system("cls")
# For clear screen
# input('Press enter to clear screen ...')

# Global varible to store user choice of answer.
user_choice = []


def main_page():
    """
    This is for user to choose whether to to take
    the survey or exit.
    """
    print('Main page')
    print()
    print()
    select = 0
    while select != 1 and select != 2:
        try:
            print(BLUE + 'Select an option: \n')
            print('1.   Take the survey\n')
            print('2.   No and exit\n')
            select = int(input('Enter your choice: '))
            print()

            if select != 1 and select != 2:
                clear_scr()
                print()
                print(RED + 'Invalid number!'.upper() + RESET)
        except ValueError:
            print(RED + 'Please enter a valid number 1 or 2' + RESET)
    if select == 1:
        # column = 1
        # options = 4
        take_survey(column, ans_options)
    else:
        # clear_scr()
        end()
    # elif select == 2:
    #     end()


# main_page()


def take_survey(column, ans_options):
    """
    To display the question and option of answer.
    Column represent the column number of question in the spreadsheet.
    Options specifies the max number of options display.
    """
    global user_choice   # Access to the global variable

    """
    Access all value from sheet q_and_a, question and answer options.
    The SHEET object retrieve data from worksheet q_and_a
    """
    data = SHEET.worksheet('q_and_a').get_all_values()

    """
    Refer to the first row of the data list.
    Column -1 is to adjust the
    """
    question = data[0][column - 1]

    # The option are retrieved from the remaining rows of the data list
    options = [row[column - 1] for row in data[1:]]

    # To generate the question and options
    print(question)
    print()
    """
    This is to iterate through the options list.
    Enumerate is a function that takes an iterable ('options' list)
    and returns an iterator that generate pairs of index and value
    for each item.
    """
    for i, option in enumerate(options, start=1):
        print(f'{i}. {options}')
        print()
        if i >= ans_options:
            # This check if True, the loop terminated using break.
            break
    # User input validation
    user_input = -1
    # This is ensure the user's choice is within the valid range.
    while user_input < 1 or user_input > ans_options:
        try:
            # Try to get user to input as an interger
            # Int convert entry to integer
            user_input = int(input('Enter your choice: '))
            if user_input < 1 or user_input > ans_options:
                print('Invalid choice. ')
                print()
                print(f'Please choose a number between 1 - {options}')
        except ValueError:
            # This block catches any exceptions error in the try block.
            print('Please enter a valid number.')
            # Processing user's choice and storing in user_choice[]
    select_option = options[user_input - 1]
    print(f'You have selected: {select_option}')
    user_choice.append(select_option)

# main_page()


def get_survey():
    """
    This functions use column as keywords
    and ans_options as values to generate all the questions
    and return a list with answer options
    """
    # Access all value from sheet q_and_a, question and answer options.
    # The SHEET object retrieve data from worksheet q_and_a   
    data = SHEET.worksheet('q_and_a').get_all_values()
    


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
    clear_scr()
    main_page()


def end():
    """
    End of survey function
    """
    select = 0
    while select != 1 and select != 2:
        try:
            print('Are you sure you want to exit?\n')
            print('1.   Yes')
            print('2.   No')
            select = int(input('Enter your choice: '))
            if select != 1 and select != 2:
                print('Invalid number! Please enter 1 or 2')
        except ValueError:
            print('Please enter a valid number.')

    if select == 1:
        goodbye_msg = SHEET.worksheet('text').col_values(3)
        print()
        print(BLUE + goodbye_msg[1].upper() + RESET)
        print()
        time.sleep(3)
        exit()
    else:
        main_page()


welcome()