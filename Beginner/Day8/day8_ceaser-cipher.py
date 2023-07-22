alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
code_word = []


def caesar(plain_text, shift_amount, dir):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if dir.lower() == "encode":
            new_position = position + shift_amount
        elif dir.lower() == "decode":
            new_position = position - shift_amount
        else:
            new_position = ""
            print("Error! Try again.")
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


caesar(plain_text=text, shift_amount=shift, dir=direction)
