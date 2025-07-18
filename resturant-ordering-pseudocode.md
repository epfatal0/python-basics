## Set up Menu

Create a menu with prices:
    burger = $5.99
    pizza  = $8.49
    salad  = $4.99
    drink  = $1.99

## Create a function to add up the total

Define a function called calculate_total(order):
    Start total at $0
    For every item and quantity in the order:
        Get the item’s price from the menu
        Multiply price by quantity
        Add to the total
    Round the total to two decimal places
    Return the total

## Begin the ordering Process

Print a welcome message (Welcome to the resturant ordering system!)
    
    Show the menu items and prices

## Take the customer's order

While user is choosing items:
    Ask what item they want
    If it’s not on the menu:
        Show error and ask again

    Ask how many they want
    If it's not a valid number or is zero or less:
        Show error and ask again

    If item is already in the order:
        Add the new quantity to the existing one
    If it’s a new item:
        Add it to the order with the quantity

    Ask if they want to add more items
    If they say no:
        Stop asking for more items

## Show order summary to the user

Use calculate_total to get the total cost
Save this order and the total into the all_orders list

Show a summary:
    For each item:
        Print how many and how much it costs
    Print the total cost

Thank the user for their order
Ask if they want to place another order
If they say no:
    Break out of the main loop


