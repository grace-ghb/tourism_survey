def age_group():
    print('What is your age?')
    age_choice = ['10-18', '19-30', '31-45', '46-60', '61 and Above']
    for index, age_range in enumerate(age_choice, start=1):
        print(f"{index}. {age_range}")    
    print()
    user_input = 0
    while user_input < 1 or user_input > len(age_choice):
        try:
            user_input = int(input("Enter your choice: "))
            if user_input >= 1 or user_input < len(age_choice):
                selected_age_range = age_choice[user_input-1]
                print(f"You have selected: {selected_age_range}")
        except ValueError:
            print("Please Enter a Valid Number.")
    print()


age_group()