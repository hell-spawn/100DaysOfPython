# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

cant1 = 0
cant2 = 0

name1 = name1.upper()
name2 = name2.upper()

cant1 = name1.count("T") + name2.count("T")
cant1 += name1.count("R") + name2.count("R")
cant1 += name1.count("U") + name2.count("U")
cant1 += name1.count("E") + name2.count("E")


cant2 += name1.count("L") + name2.count("L")
cant2 += name1.count("O") + name2.count("O")
cant2 += name1.count("V") + name2.count("V")
cant2 += name1.count("E") + name2.count("E")

score = (cant1 * 10) + cant2 

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
