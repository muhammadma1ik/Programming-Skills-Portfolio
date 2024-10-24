# Defining a list of countries with their corresponding capitals as tuples
quiz_data = [
    ("France", "Paris"),
    ("Switzerland", "Bern"),
    ("Germany", "Berlin"),
    ("Italy", "Rome"),
    ("Spain", "Madrid"),
    ("Romania", "Bucharest"),
    ("Greece", "Athens"),
    ("Poland", "Warsaw"),
    ("Belgium", "Brussels"),
    ("UK", "London")
]

# Creating a variable to track the number of correct answers given by user
score = 0

# Creating a for loop to iterate through each tuple in the quiz_data list
# Values from each tuple are assigned to the variables 'country' and 'capital'
for country, capital in quiz_data:
    user_answer = input(f"What is the capital of {country}? ") # Quizzes the user for the capital of the current country

    # Check if the answer is correct (ignoring capitalization) using "==" comparison operator and string methods
    if user_answer.lower() == capital.lower():
        print("Correct!")   # Informs the user that their answer is correct and the next line increments the value of score
        score += 1  
    else:
        print(f"Wrong! The correct answer is {capital}.")   # informs the user that their answer is wrong and also outputs the correct answer

# Displays the final scores of the Quiz
print(f"You got {score} out of {len(quiz_data)} correct!")
