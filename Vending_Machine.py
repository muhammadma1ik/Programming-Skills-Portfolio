# Main program function
def main():
    """
    1.The main function runs the vending machine program.
    2. It continuously displays the menu, allows user to select items, facilitates the payment process,
    and generates a receipt for purchased items"
    """
    while True:
        display_menu() #Shows the menu of available items
        selected_items = user_selection() # Allows the user to choose items
        if selected_items: # The if statement ensures that the program proceeds only if the items are selected
            total_price = display_payment(selected_items)
            if process_payment(total_price):
                generate_receipt(selected_items, total_price) #prints the receipt
        else:
            print("\nNo items purchased. Returning to menu.") # Informs the user that no items were selected

# Items dictionary
items = {
    1: {"itemID": "12", "itemCategory": "Drink", "itemName": "Water", "itemPrice": 1.00, "itemQuantity": 20},
    2: {"itemID": "13", "itemCategory": "Drink", "itemName": "Mountain Dew", "itemPrice": 2.50, "itemQuantity": 7},
    3: {"itemID": "14", "itemCategory": "Drink", "itemName": "Red Bull", "itemPrice": 9.50, "itemQuantity": 3},
    4: {"itemID": "15", "itemCategory": "Drink", "itemName": "Coffee", "itemPrice": 4.00, "itemQuantity": 10},
    5: {"itemID": "16", "itemCategory": "Snack", "itemName": "Protein Bar", "itemPrice": 8.00, "itemQuantity": 6},
    6: {"itemID": "17", "itemCategory": "Snack", "itemName": "Lays Salted Chips", "itemPrice": 3.00, "itemQuantity": 4},
}

# Suggestions dictionary; stores the mapped items to suggested items
suggestions = {
    "Water": "Lays Salted Chips",
    "Mountain Dew": "Protein Bar",
    "Red Bull": "Lays Salted Chips",
    "Coffee": "Protein Bar",
    "Protein Bar": "Mountain Dew",
    "Lays Salted Chips": "Water"
}

# Function to display the vending machine menu
def display_menu():
    """
    1. This function displays the main menu of the vending machine.
    2. It separates the items by category (Drinks or Snacks) and also shows
    the Item ID, name, price, and available quantity.
    """
    print("=" * 50)
    print("               📜 VENDING MACHINE MENU 📜               ")
    print("=" * 50)

    # Displays items in the "Drinks" Category
    print("\n🍹 Drinks:")
    for code, item in items.items():
        if item["itemCategory"] == "Drink":
            print(f"{item['itemID']}: {item['itemName']} - ${item['itemPrice']} ({item['itemQuantity']} in stock)")

    # Displays items in the "Snacks" Category
    print("\n🍴 Snacks:")
    for code, item in items.items():
        if item["itemCategory"] == "Snack":
            print(f"{item['itemID']}: {item['itemName']} - ${item['itemPrice']} ({item['itemQuantity']} in stock)")
    print("=" * 50)

# This Function's role is to handle and manage user selection
def user_selection():
    """
    1. Allows the user to select items from the vending machine.
    2. Prompts for an item ID and quantity.
    3. Validates the input and checks stock availability.
    4. Suggests additional items based on user's previous choice to enhance user experience.
    5. Returns a list of selected items with their quantities and prices.
    """
    selected_items = [] # This list will be used to store items selected by the user

    while True:
        item_id = input("\nEnter the ID of the item to add to your cart (or '0' to proceed to payment): ").strip()

        if item_id == '0':  # This exits selection if the user chooses to
            if selected_items:
                break
            else:
                print("❌ No items selected. Please choose at least one item.") # Error Message
        else:
            # Locates the item in the items dictionary using its ID
            item = next((item for item in items.values() if item["itemID"] == item_id), None)
            if item and item["itemQuantity"] > 0: # Checks if the item exists and is in stock
                # prompts the user for the quantity of the selected item
                quantity = int(input(f"Enter the quantity of {item['itemName']} (available: {item['itemQuantity']}): "))
                if 0 < quantity <= item["itemQuantity"]: # This if statement validates quantity
                    # Adds the selected items to cart
                    selected_items.append({"Name": item["itemName"], "Price": item["itemPrice"], "Quantity": quantity})
                    item["itemQuantity"] -= quantity # Updates stock
                    print(f"✔️ Added {quantity}x {item['itemName']} to your cart.")

                    # Suggests another item based on what user previously selected
                    suggestion = suggestions.get(item["itemName"])
                    if suggestion:
                        print(f"🤔 Suggestion: Would you like to add {suggestion}?")
                        add_suggestion = input("Enter 'yes' to add it or 'no' to skip: ").strip().lower()
                        if add_suggestion == "yes":
                            suggested_item = next((item for item in items.values() if item["itemName"] == suggestion), None)
                            if suggested_item and suggested_item["itemQuantity"] > 0:
                                selected_items.append({"Name": suggested_item["itemName"], "Price": suggested_item["itemPrice"], "Quantity": 1})
                                suggested_item["itemQuantity"] -= 1 # Updates stock
                                print(f"✔️ Added 1x {suggested_item['itemName']} to your cart.")
                            else:
                                print(f"❌ Sorry, {suggestion} is out of stock.") # Informs user if the suggested item is now out of stock
                else:
                    print(f"❌ Invalid quantity. Please select between 1 and {item['itemQuantity']}.") # Handles Quantity Error
            else:
                print("❌ Invalid item ID or out of stock.") # Handles all other errors; including invalid input, invalid ID or out of stock item

    return selected_items # Returns the list of selected items

# This function calculates and displays the payment summary
def display_payment(selected_items):
    """
    1. Calculates the total price of selected items and displays a payment summary.
    2. Provides a breakdown of items, quantities, and prices.
    3. Returns the total cost of all selected items.
    """
    print("\n" + "=" * 50)
    print("               💰 PAYMENT SUMMARY 💰               ")
    print("=" * 50 + "\n")

    # Calculates the Total Price
    total_price = sum(item["Price"] * item["Quantity"] for item in selected_items)
    # Displays the itemized details
    for item in selected_items:
        print(f"{item['Name']} - {item['Quantity']}x @ ${item['Price']} each = ${item['Price'] * item['Quantity']:.2f}")
    print("\n" + "-" * 50)
    print(f"Total Price: ${total_price:.2f}")
    print("=" * 50 + "\n")
    return total_price # Returns the total price

# This Function is used to facilitate the payment process
def  process_payment(total_price):
    """
    1. Handles payment by accepting money from the user.
    2. Validates input and ensures if the money inserted is sufficient, if not, it informs the user.
    3. Calculates and displays change.
    4. Returns True if payment is successful.
    """
    while True:
        try:
            # Prompts user to insert money
            money_inserted = float(input("\nInsert money: $"))

            if money_inserted >= total_price: # Checks if the payment is sufficient
                change = money_inserted - total_price # Calculates Change
                print(f"✔️ Payment accepted! Your change is ${change:.2f}.")
                return True # Payment Successful
            else:
                # Notifies user of insufficient funds and informs the user on how much more is required
                print(f"❌ Insufficient funds! You need ${total_price - money_inserted:.2f} more.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid amount.") # handles invalid input

# Function to generate a receipt
def generate_receipt(selected_items, total_price):
    """
    1. Generates a receipt for purchased items.
    2. Displays itemized details, total cost, and a thank-you message.
    """
    print("\n" + "=" * 50)
    print("                  🧾 RECEIPT 🧾                   ")
    print("=" * 50 + "\n")

    # Displays purchased Items
    for item in selected_items:
        print(f"{item['Name']} - {item['Quantity']}x @ ${item['Price']} each = ${item['Price'] * item['Quantity']:.2f}")
    print("\n" + "-" * 50)
    print(f"Total Price: ${total_price:.2f}")
    print("\n✔️ Thank you for your purchase! Have a great day.")
    print("=" * 50 + "\n")

# Run the vending machine
if __name__ == "__main__":
    main() # Initiates the vending machine program