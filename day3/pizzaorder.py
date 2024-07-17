# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Thank you for choosing Python Pizza Deliveries!")

#Original prices
S = 15
M = 20
L = 25
#Additional prices
S_pepperoni = 2
M_pepperoni = 3
L_pepperoni = 3

cheese = 1

#Get user input

size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill = S
elif size == "M":
    bill = M
elif size == "L":
    bill = L
else:
    print("Unrecognised input, please use S, M or L in capital letters!")

#add pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill += S_pepperoni
    elif size == "M":
        bill += M_pepperoni
    elif size == "L":
        bill += L_pepperoni

#add cheese
if extra_cheese == "Y":
    bill += cheese
print(f"Your final bill is ${bill}")







