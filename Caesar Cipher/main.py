import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "encode":
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
                continue
            new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
        print(f"Here is the encoded result: {cipher_text}")
    decipher_text = ""
    if encode_or_decode == "decode":
        for letter in original_text:
            if letter not in alphabet:
                decipher_text += letter
                continue
            new_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            decipher_text += alphabet[new_position]
        print(f"Here is the decoded result: {decipher_text}")
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    user_input = input("Type YES if you want to go again. Otherwise, type NO.\n").lower()
    if user_input != "yes":
        print("GOOD BYE")
        break







