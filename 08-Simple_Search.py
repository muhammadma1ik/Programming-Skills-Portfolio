# Defining the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# We are searching for "Sam" so the search_term is defined as "Sam"
search_name = "Sam"

# Step 3: Search for the term in the list
if search_name in names:
    print(f"{search_name} is found in the list.")
else:
    print(f"{search_name} is not found in the list.")