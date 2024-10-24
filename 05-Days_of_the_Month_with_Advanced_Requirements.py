# Defining a dictionary where the keys are the month numbers and the values are the number of days in those months
days_in_a_month = {
    1: 31, 
    2: 28,  # February has 28 days in a non-leap year
    3: 31,  
    4: 30,  
    5: 31,  
    6: 30,  
    7: 31,  
    8: 31,  
    9: 30,  
    10: 31, 
    11: 30, 
    12: 31  
}

# Asks the user the input the month number and converts the input into an integer
month_number = int(input("Enter the month number (1-12): "))

# This Checks if the month number inputted by the user is valid using an if condition
if month_number < 1 or month_number > 12:
    print("Invalid month number! Please enter a number between 1 and 12.") # informs the user that the month number is invalid
else:
    # Checks if the month is february
    if month_number == 2:
        # Ask the user if the year is a leap year (leap year adjustment)
        leap_year = input("Is it a leap year? (yes/no): ").strip().lower() # using string methods to remove extra space and standardize input to lowercase
        # Check the user's response and print the number of days
        if leap_year == 'yes':
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days in a non-leap year.")
    else:
        # For other months, the number of days are printed using the dictionary
        print(f"The month number {month_number} has {days_in_a_month[month_number]} days.")
