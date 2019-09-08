# Initializing variables to no value at the top
cost = None
payment = None
change = None
loop = True


# Function to ask for subtotal and payment
def ask_value():
    temp_cost = eval(input("How much is your subtotal?"))
    temp_pay = eval(input("How much are you paying?"))
    return temp_cost, temp_pay


# Function to calculate how many of each coins the customer will receive in change
def coin_calc(coin_val, change_amount):
    num_of_coins = change_amount // coin_val
    return num_of_coins


# Main portion of the class
while loop:
    cost, payment = ask_value()
    change = payment - cost
    while change < 0:
        print("You need to pay more than what is owed, try again.")
        cost, payment = ask_value()
        change = payment - cost

    change_print = change
    change = change * 100

    # Calculations for the numbers of each coin, changing the value of change after each calculation
    quarters = coin_calc(25, change)
    change = change - quarters * 25
    dimes = coin_calc(10, change)
    change = change - dimes * 10
    nickels = coin_calc(5, change)
    change = change - nickels * 5
    pennies = coin_calc(1, change)

    print("The amount due was: ", cost)
    print("The amount you gave was: ", payment)
    print("Your change in coins is: ")
    print("Quarters: ", int(quarters))
    print("Dimes: ", int(dimes))
    print("Nickels: ", int(nickels))
    print("Pennies: ", int(pennies))
    total_coins = quarters + dimes + nickels + pennies
    print("Your total number of coins is: ", int(total_coins))
    print("The total value of your change is: ", '${:,.2f}'.format(change_print))
    cont = input("Would you like to calculate another exchange? [y/n]")
    if cont == "y":
        loop = True
    else:
        loop = False
