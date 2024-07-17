#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.

number = int(input("Enter the number to check: "))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")



