#Instructions

#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#https://waitbutwhy.com/2014/05/life-weeks.html
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:

#    You have x days, y weeks, and z months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(6 + 4 / 2 - (1 * 2))

yearsLeft = 90 - int(age)
days =  yearsLeft * 365
weeks = yearsLeft * 52
months = yearsLeft * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

