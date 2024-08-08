def encrypt(original_text, shift):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabets:
            shifted_pos = alphabets.index(letter) + shift
            shifted_pos = shifted_pos % len(alphabets)
            cipher_text += alphabets[shifted_pos]
        else:
            cipher_text += letter
    print(f"Here is the encoded version: {cipher_text}")


def decrypt(original_text, shift):
    deciphered_text = ""
    for letter in original_text:
        if letter in alphabets:
            shifted_pos = alphabets.index(letter) - shift
            shifted_pos = shifted_pos % len(alphabets)
            deciphered_text += alphabets[shifted_pos]
        else:
            deciphered_text += letter
    print(f"Here is the decoded version: {deciphered_text}")


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    original_text = input("Enter the text:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(original_text, shift)
    elif direction == "decode":
        decrypt(original_text, shift)
    else:
        print("Invalid input, please type 'encode' to encrypt or 'decode' to decrypt.")

    restart = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if restart != "yes":
        print("Goodbye!")
        break
