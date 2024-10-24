# Defining the correct password
password = "12345"

# Defining the number of attempts & also the max number of attempts allowed
attempts = 0
max_attempts = 5

# Initiating a while loop to ask the user for the correct password while keeping into account the number of attempts
while attempts < max_attempts:
    entered_password = input("Please enter the password: ")
    if entered_password == password:   # Checks if the entered password is correct
        print("Access granted.")
        break  # The loop is exited when the password entered is correct
    else:
        # Increments the attempts counter if the password entered was wrong
        attempts += 1
        remaining_attempts = max_attempts - attempts  
        print(f"Incorrect password. You have {remaining_attempts} attempts remaining.") # Informs the user of remaining attempts
        
# Checks if the maximum number of attempts has been reached
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")