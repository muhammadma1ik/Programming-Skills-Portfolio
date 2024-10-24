"""
 Creating a Function to determine if a number is even or odd,
 which then returns a message indicating whether the number is even or odd.
"""
def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    # Asks for user input to input an number 
    user_input = input("Enter a number: ")

    # Converts the input to an integer
    number = int(user_input)

    # Calls the function to check if the number is even or odd
    result = check_even_or_odd(number)

    # Messge returned from the function is printed
    print(result)

main() #calling main function to run the program
