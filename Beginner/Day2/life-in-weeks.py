# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Hard code expected year of death on 90th birthday, buuuttt make it a variable juust in case
# we want to change it later.
deathAge = 90
yearsLeft = deathAge - int(age)
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left")
