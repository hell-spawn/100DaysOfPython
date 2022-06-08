# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
# Don't use len() or sum()

#Write your code below this row 👇

summation = 0
count = 0
average = 0
for height in student_heights:
    summation += height
    count+=1

average = round(summation / count)
print(average)
