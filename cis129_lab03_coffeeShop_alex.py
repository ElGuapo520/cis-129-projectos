# Program Title: Alex's Coffee Shop
# Author: Alex J. Garcia Suarez
# Date: Feb-17-2024
# Course: CIS129 Pima Community College Spring 2024
# Assignment : Module 3 lab : Coffee Shop Receipt
# Description: This Python program generates a receipt for a coffee and muffin shop based on user input.
########################################################################################################

    # Function Definitions

def calculate_total(coffee_count, muffin_count, tea_count, cookie_count): 
    """
    Calculates the subtotal, tax amount, and total amount based on the number of coffees and muffins purchased.

    Args:
        coffee_count (int): The number of coffees purchased. 
        muffin_count (int): The number of muffins purchased.
        tea_count (int): The number of teas purchased.
        cookie_count (int): The number of cookies purchased.



    Returns:
        tuple: A tuple containing the subtotal, tax amount, and total amount.
    """
    coffee_price = 5 
    muffin_price = 4
    tea_price = 2
    cookie_price = 1
    
    tax_rate = 0.06

    coffee_cost = coffee_count * coffee_price 
    muffin_cost = muffin_count * muffin_price
    tea_cost = tea_count * tea_price 
    cookie_cost = cookie_count * cookie_price 
    subtotal = coffee_cost + muffin_cost + tea_cost + cookie_cost
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    return subtotal, tax_amount, total


def print_receipt(coffee_count, muffin_count, tea_count, cookie_count, subtotal, tax_amount, total):
    """
    Prints the receipt with the provided information.

    Args:
        coffee_count (int): The number of coffees purchased.
        muffin_count (int): The number of muffins purchased.
        subtotal (float): The subtotal of the purchase.
        tax_amount (float): The tax amount.
        total (float): The total amount including tax.
    """
    print("***************************************")
    print("Alex's Cafe Receipt")
    print(f"{coffee_count} Coffee at $5 each: ${coffee_count * 5:.2f}") #f =format aka f-string
    print(f"{muffin_count} Muffins at $4 each: ${muffin_count * 4:.2f}") #.2f =  fornat 2 decimal places
    print(f"{tea_count} tea at $2 each: ${tea_count * 2:.2f}") 
    print(f"{cookie_count} cookies at $1 each: ${cookie_count * 1:.2f}") 
    print(f"6% tax: ${tax_amount:.2f}")
    print("---------------------------------------")
    print(f"Total: ${total:.2f}")
    print("***************************************")


    # Main Function
    
def main():
    """
    Main function of the program.
    """
    print("***************************************")
    print("Alex's Cafe")
    coffee_count = int(input("Number of coffees bought?  ")) # prompt user for input of number of coffees bought
    muffin_count = int(input("Number of muffins bought?  ")) # prompt user for input of number of muffins bought
    tea_count = int(input("Number of teas bought?  ")) # prompt user for input of number of teas bought
    cookie_count = int(input("Number of cookies bought?  ")) # prompt user for input of number of cookies bought
    subtotal, tax_amount, total = calculate_total(coffee_count, muffin_count, tea_count, cookie_count) # call calculate_total function and store the returned values in variables
    print_receipt(coffee_count, muffin_count, tea_count, cookie_count, subtotal, tax_amount, total) # call print_receipt for number of coffees, muffins, tea, cookies, subtotal, tax amount, and total amount
    print("\n Thank you, Come again :)  \n\n")
   
   


# Call the main function
    
if __name__ == "__main__":
    main()
