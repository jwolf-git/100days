# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

both_names = name1.lower() + name2.lower()

count1 = both_names.count("t")
count1 += both_names.count("r")
count1 += both_names.count("u")
count1 += both_names.count("e")

count2 = both_names.count("l")
count2 += both_names.count("o")
count2 += both_names.count("v")
count2 += both_names.count("e")

name_total = int((str(count1) + str(count2)))

if name_total < 10 or name_total > 90:
    result = ", you go together like coke and mentos."
elif 40 <= name_total <= 50:
    result = ", you are alright together."
else:
    result = "."

print(f'"Your score is " {name_total} {result}')
