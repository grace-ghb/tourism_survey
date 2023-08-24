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


planning()