# Getting User Inputs for name, hometown and age   
name = input("Please enter your Full name (first and last): ")
hometown = input("Please enter your Hometown: ")
age = input("Please enter your Age: ")

# This checks if the input given for age is numeric
if age.isdigit():
    age = int(age)  # This Converts the string input to integer if input was valid
    
    #Storing the information inputted in a dictionary
    person_info = {
        "name": name,         # The key 'name' stores the value of the name variable
        "hometown": hometown,  # The key 'hometown' stores the value of the hometown variable
        "age": age            # The key 'age' stores the value of the age variable as inputted by the user
    }

    # Printing the values on separate lines using line breaks
    print(f"\nName: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")
else:
    # This informs the user that the input they gave for the variable age was invalid
    print("Invalid input. Please enter a numeric value for age.")
