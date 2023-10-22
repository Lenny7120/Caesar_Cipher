#!/usr/bin/python3

"""This is a simple code which shows how a Caesar Cipher works"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text, shift_key):  # define the encryption function
    cipher_text = ""  # create an empty string to hold the encrypted text
    for char in plain_text:  # iterate using for loop to get the index of the alphabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26  # using this formular you get the new position of the text
            cipher_text += alphabet[new_position]  # you store the new alphabet in the empty string you created
        else:
            cipher_text += char  # else any other symbols, numbers and space will be added but not affected
    print(f"Here is the encryption message:\n {cipher_text}")  # print the output


"""Same for the decryption but in reverse"""


def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the decryption message:\n {plain_text}")


end = False  # create a Flag to stop the loop when needed
while not end:
    # accept input from the users
    text = input("Type 'encrypt' for encryption, Type 'decrypt' for decryption\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Enter shift key:\n"))
    if text == 'encrypt':  # using the if conditionals explains what happens when you chose encrypt and vice versa
        encryption(plain_text=message, shift_key=shift)
    elif text == 'decrypt':
        decryption(cipher_text=message, shift_key=shift)
    play_again = input("Type 'yes' to continue or 'no' to exit:\n").lower()  # if you want to continue
    if play_again == 'no':
        end = True  # the Flag to end the program
        print("End of Program")

