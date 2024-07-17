# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."

print("Velkom!, The Love Calculator is calculating your score...")
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

#combine both names
both_names = name1 + name2

#use a function to avoid errors originating from user upper or lower case
lower_names = both_names.lower()

#count the number of letters existing in the combined names
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u+ e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

#concatenate the numbers from both names
score = str(first_digit) + str(second_digit)

#convert the numbers to integers for conditioning
love_score = int(score)

if (love_score < 10 )or (love_score >90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score > 40 ) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {score}.")





