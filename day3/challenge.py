# Challenge: Advanced Pizza Order Program

# Requirements:
# Pizza Sizes and Prices:
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Toppings and Prices:
# Pepperoni: +$2 for small, +$3 for medium/large
# Mushrooms: +$1
# Extra cheese: +$1.5

# Discount Codes:
# DISCOUNT10 for 10% off the total bill
# DISCOUNT20 for 20% off the total bill

small = 15
medium = 20
large = 25
peppsmall = 2
peppmedium = 3
pepplarge = 3
mashroom = 1
cheese = 1.5

code10 = 0.1
code20 = 0.2

bill = 0

print("Hooray! Welcome to MomsTouch! Please proceede to make your order!")

size = input("Enter your order size S for small, M for medium or L for large: ")
with_pepp = input("Would you like it with pepperoni?, Y or N: ")
with_mashroom = input("Would you like it with mashroom?, Y or N: ")
with_cheese = input("Would you like it with cheese?, Y or N: ")
code = input("please enter your discount code DISCOUNT10 or DISCOUNT20: ")

#size prompt
if size == "S":
    bill = small
elif size == "M":
    bill = medium
elif size == "L":
    bill = large

#pepperoni prompt
if with_pepp == "Y":
    if size == "S":
        bill += peppsmall
    elif size  == "M":
        bill += peppmedium
    elif size == "L":
        bill += pepplarge

#mashroom prompt
if with_mashroom == "Y":
    bill += mashroom

#cheese prompt
if with_cheese == "Y":
    bill += cheese

#discount prompt
if code == "DISCOUNT10":
    discount = bill * code10
elif code == "DISCOUNT20":
    discount = bill * code20

else:
    discount = 0

    bill -= discount

print(f"Your final bill is ${bill}.")



