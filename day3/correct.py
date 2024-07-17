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

print("Hooray! Welcome to MomsTouch! Please proceede to make your order!")

size = input("Enter your order size S for small, M for medium or L for large: ")
with_pepp = input("Would you like it with pepperoni?, Y or N: ")
with_mashroom = input("Would you like it with mashroom?, Y or N: ")
with_cheese = input("Would you like it with cheese?, Y or N: ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if with_pepp == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if with_mashroom == "Y":
    bill += 1

if with_cheese == "Y":
    bill += 1.5


print(f"Your final bill is ${bill}")




