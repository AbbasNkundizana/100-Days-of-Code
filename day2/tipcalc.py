#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
#Write your code below this line 

bill = float(input("Enter total bill: "))
tip = float(input("Enter percent of tip you want to offer: "))
tippercent = tip / 100
heads = int(input("Enter number of persons: "))
tipbill = bill * tippercent
totalbill = bill + tipbill

individual = totalbill / heads

print(f"Your individual contribution is {individual: .2f}")