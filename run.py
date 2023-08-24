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


# Connect Pandas to Google Sheets.
data = SHEET.worksheet('survey_answer').get_all_values()
headers = data.pop()    # Remove headers row, assign to var headers.
df = pd.DataFrame(data, columns=headers)     # Columns extract from headers.
df.head()   # To get a glimpse of DataFrame's structures and contents


RED = Fore.RED      # Red color text
YELLOW = Fore.YELLOW    # Yellow color text
BLUE = Fore.BLUE    # Blue color text
RESET = Style.RESET_ALL     # Resets all the color to default
BRIGHT = Style.BRIGHT       # Text bright

# To access the data in the worksheet, parameter name same as sheet name.
text = SHEET.worksheet('text')
# q_and_a = SHEET.worksheet('q_and_a')
# survey_answer = SHEET.worksheet('survey_answer')
# To pull all values from the sheet.
data = text.get_all_values()
# data2 = q_and_a.get_all_values()
# data3 = survey_answer.get_all_values()
print(data)
print()
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


def display_questions_and_options(column):
    """
    To generate questions and options
    """
    data = SHEET.worksheet('q_and_a').get_all_values()
    """
    The code access the first row of the 'data'
    which contains the header of each column
    Extract the question from the header row
    """
    question = data[0][column - 1]
    """
    This list iterates through each row in 'data'
    starting from the second row (index 1).
    Extracts the options from the data row.
    """
    options = [row[column - 1] for row in data[1:]]

    print(question)
    for i, option in enumerate(options, start=1):
        print(f'{i}. {option}')
    print()


def get_survey():
    """
    From sheet q_and_a
    To generate all the questions for the survey
    """
    data = SHEET.worksheet('q_and_a')   # Retrieves the worksheet
    # Creates a DataFrame using the data retrieved from 'q_and_a'
    df_answers = pd.DataFrame(data[1:], columns=data[0])
    #Calculates the number of columns in the DataFrame
    column_keys = len(df_answers.columns)

    for column in range(1, column_keys + 1):
        display_questions_and_options(column)
    
    submit_option()


# get_survey()


def update_answer():
    """
    This is to update the user's answer into the sheet survey_answer
    """
    print('Updating result, please wait...\n')
    SHEET.worksheet('survey_answer').append_row(data)
    print('The result updated.\n')


# update_answer()


def submit_option():
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


# submit_option()


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

            if select != 1 and select != 2:
                print('Invalid Number!')
        except ValueError:
            print('Please enter a valid number 1 or 2')
    if select == 1:
        display_questions_and_options(column)
    elif select == 2:
        end()


# main_page()


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


# welcome()


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