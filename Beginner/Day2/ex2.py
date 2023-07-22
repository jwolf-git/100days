# Changing data types - you can only concat strings together

num_char = len(input("whats your name? "))

str_num_char = str(num_char)

print("your name has " + str_num_char + " characters")

# adding variables inside print, then print function will convert the result and print
print(10 + float(80.5))

# this will convert to string and then concat the result
print(str(10)+ str(80.5))
