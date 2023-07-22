# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_len = nr_letters + nr_symbols + nr_numbers
password = []

for pw_char in range(0, nr_letters):
    chosen_char = letters[random.randint(0, len(letters)-1)]
    password.insert(random.randint(0, total_len), chosen_char)

for pw_char in range(0, nr_symbols):
    chosen_char = symbols[random.randint(0, len(symbols)-1)]
    password.insert(random.randint(0, total_len), chosen_char)

for pw_char in range(0, nr_numbers):
    chosen_char = numbers[random.randint(0, len(numbers)-1)]
    password.insert(random.randint(0, total_len), chosen_char)


password = ''.join(password)
print("Your password is: " + password)
