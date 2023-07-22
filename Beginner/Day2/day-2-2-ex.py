# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# BMI calculation, height / weight^2
# Make them both float from string because input is in strings
bmi = (float(weight) / (float(height) ** 2))
# Print the result, convert back to string, so you can concat the percent sign, also round to tenth
print(str(round(bmi, 1)) + "%")
