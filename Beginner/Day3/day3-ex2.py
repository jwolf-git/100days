# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round((weight / (height ** 2)), 1)

if bmi < 18.5:
    bmi_value = "are underweight."
elif bmi < 25:
    bmi_value = "have a normal weight."
elif bmi < 30:
    bmi_value = "are slightly overweight."
elif bmi < 35:
    bmi_value = "are obese."
else:
    bmi_value = "are clinically obese."

print(f"Your BMI is {int(bmi)}, you {bmi_value}")
