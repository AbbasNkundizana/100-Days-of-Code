#write a body mass index calculator code
#body mass index is the ratio of body weight in kg to the square of body height in m

weight = float(input("Enter weight: "))
height = float(input("Enter height in meters: "))

BMI  = int(weight / (height ** 2))

print(BMI)
