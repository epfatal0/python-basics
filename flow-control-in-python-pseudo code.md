# Create a menu of items with prices
SET items TO {
    "soda": 1.50,
    "chips": 2.00,
    "candy": 1.00,
    "cookies": 2.00
}

# Ask user how much money they have
DISPLAY "How much money do you have? $"
GET user input as balance_input

#  Check if input is a valid number
IF balance_input is a valid number (digits or decimal)
    CONVERT balance_input TO float
ELSE
    DISPLAY "Invalid. Please start over."
    STOP program

#  Show menu
DISPLAY "Menu:"
FOR each item and price in items
    DISPLAY item name with first letter capitalized and the price

#  Start loop
WHILE True DO
    DISPLAY "Money left: $" + balance 

    # Ask user what they want
    DISPLAY "Pick an item or type 'exit':"
    GET user input their choice
    CONVERT choice to lowercase

    #  Exit if user types "exit"
    IF choice IS "exit"
        DISPLAY "Thanks for visiting!"
        BREAK the loop

    # If choice is not on the menu
    IF choice is NOT in items
        DISPLAY "Not on menu. Try again."
        CONTINUE to next loop

    # Get item price
    SET price TO items[choice]

    #  Check if user can afford it
    IF balance >= price
        SUBTRACT price from balance
        DISPLAY "You bought" + choice + "for $" + price
    ELSE
        DISPLAY "Not enough money."

    # Check if user can afford anything else
    IF balance is less than the cheapest item
        DISPLAY "You don't have enough for anything else."
        BREAK the loop

# End: show final balance
DISPLAY "Final balance: $" + balance 
