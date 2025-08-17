"""
Problem Statement
You have x no. of 5 rupee coins and y no. of 1 rupee coins.
You want to purchase an item for amount z.
The shopkeeper wants you to provide exact change.
You want to pay using minimum number of coins.
How many 5 rupee coins and 1 rupee coins will you use?
If exact change is not possible then display -1.
"""

def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    five_needed = min(rupees_to_make // 5, no_of_five)
    remaining_amount = rupees_to_make - (five_needed * 5)

    if remaining_amount <= no_of_one:
        one_needed = remaining_amount
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)

# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28, 8, 5)