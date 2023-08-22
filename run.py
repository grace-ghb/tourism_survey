"""
To import the entire gspread library so we access any class 
function or method within it.
Import credentials class which is part of the service account
function from the google oauth library.
"""
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) # To initialize the colorama library
import os   #To use for clear screen
import time

# List the API that the program should access in order to run
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

RED = Fore.RED  # Red color text
YELLOW = Fore.YELLOW    # Yellow color text
BLUE = Fore.BLUE    # Blue color text
RESET = Style.RESET_ALL #Resets all the color to default
BRIGHT = Style.BRIGHT   #Text bright

# To access the data in the worksheet, parameter name same as sheet name.
text = SHEET.worksheet('text')

#To pull all values from the sheet.
data = text.get_all_values()

def clear_scr():
    """
    This function is for clear screen for different OS
    """
    # if os.name == "posix":
    #     _ = os.system("clear")
    # else:
    #     _ = os.system("cls")

    os.system('cls' if os.name == 'nt' else 'clear')

# For clear screen
# input('Press enter to clear screen ...')

# Call the clear_scr funtion to clear the terminal
clear_scr()


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
welcome()


def take_survey():
    """
    This is for user to choose whether to to take
    the survey or exit.
    """
    select = 0
    while select != 1 and select != 2:
        try:
            print(BLUE + 'Select an option: \n')
            print('1.   Take the survey\n')
            print('2.   No and exit\n')
            select = int(input('Enter your choice: '))

            if select != 1 and select != 2:
                clear_scr()
                print()
                print(RED + 'Invalid number!'.upper() + RESET)
                print()
                
        except ValueError:
            print(RED + 'Please enter a valid number 1 or 2' + RESET)

take_survey()



def end():
    """
    End of survey function
    """
    goodbye = SHEET.worksheet('text').col_values(3)
    print()
    print(BLUE + goodbye[1].upper() + RESET)
    print()    

end()


