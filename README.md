# Tourism Survey
Developer: Grace

Tourism Survey is a project configure using python, there are question and answer options where the result will be append link to Google spreadsheet. There are text messages retrieved from Google spreadheet and all these are through Google API connect link between two programm - Python and Google spreadsheet. 

To view the project click [here](https://tourism-survey-02c2e85cb97f.herokuapp.com/).

## Table of Contents
1.	User Experience (UX)
	-   Project Goals
	-   User Stories
	-   Typography
	Wireframes
2.	Design
	-   Typography
	-   Wireframes
    -   Features
3.	Techologies Used
    -    Languages Used
    -    Frameworks, Libraries & Programs Used
4.	Testing
o	W3C Validator
o	Accessibility
o	Home Page
o	Menu Page
o	Gallery Page
o	Contact Us Page
o	Sign Up Page
o	Tools Testing
o	General Testing
5.	Finish Products
o	Home Page
o	Menu Page
o	Gallery Page
o	Contact Us Page
o	Sign Up Page
6.	Deployment
o	GitHub Pages
7.	Credits
o	Content
o	Code
o	Acknowledgments
 
# User Experience (UX)

## Project Goals
- Collect user demographic information.
- Collect user answer for the survey.
- Store the result data in Google spreadsheet.
- Show the questions and answer options.
- To validate that the Google API link between two program here, Python and Google spreadsheet.


## User stories

- As a user I would like to understand the purpose of the survey.
- As a user I would like to choose whether to take the survey or not.
- As a user I would like to have an option to choose from the answer.
- I might have a typo error when enter the choose number, as a user I would like to be inform and try again.
- As a user I would like to have an option to submit the survey or not.
- As a user I would like to have an option to choose to confirm exit or change my mind to take the survey.

Back to [Table of Contenets](#table-of-contents)


## Data Model

- This program uses Google sheet to retrieve text information and to store result from the survey.

- The welcome message and the goodbye message are store in the Google sheet.

- The user_choice variable is use to store data in the Google sheet.

- This is the Google sheet used to stored text message

![Text worksheet](images/wk-text.png)

- This is the Google sheet used to stored survey results.
![]()


## Flowchart

I use [Diagrams](https://app.diagrams.net/) to create flowchart for my project. 

![Flowchart](images/flowchart.png)


# Features

## Title Screen

- This screen show the welcome home page with system loading message informing user to wait during the process

![Welcome home page](images/welcome-home-page.png)

- The below two screeshot are welcome meassage screen with introductory about the survey.
- User have press enter to continue to the next screen.

![Welcome introductory - 1](images/welcome-1.png)

![Welcome introductory - 2](images/welcome-2.png)


## Option

- This screen gives the user to choose to 
    - Take the survey
    - No and Exit

![Select option](images/select-option.png)

## Taking the Survey

- This part of the program shows the questions and the answer options for the user to choose.
- User have to enter their choice number at "Enter your choice" and below will show the answer which the user have choose.
- If the user choose the number which is out of the range red warning message "Invalid input! Please try again" will print out and the message "Enter your choice" will print out again for the user to retype their correct choice.

![Question 1](images/q1.png)
![Question 2](images/q2.png)
![Question 3](images/q3.png)
![Question 4](images/q4.png)
![Question 5](images/q5.png)
![Question 6](images/q6.png)
![Question 7](images/q7.png)
![Question 8](images/q8.png)
![Question 9](images/q9.png)
![Question 10](images/q10.png)
![Question 11](images/q11.png)

![]()
![]()
![]()



Back to Table of Contents
Top
 