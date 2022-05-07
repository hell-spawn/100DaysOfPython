# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):



# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(weight) / (float(height) ** 2 )
bmi =round(bmi)

print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")
