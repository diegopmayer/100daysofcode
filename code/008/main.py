# Ceasar Cipher solution
# it´s a incription solution added by a number in each letter.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z']*2

def ceaser_cipher(direction, alphabet, text, shift):
    
    cipher_text = ''
    if direction == 'decode':
        shift *= -1 

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The {direction}d text is {cipher_text}")

again=True
while again:
    # asking questions
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    # calling the function
    ceaser_cipher(direction, alphabet, text, shift)
    # calling action to do againa or stop the function
    yes = input(
        "Type 'yes' if you want to go again. Otherwise type 'no': "
        ).lower()
    if yes == 'yes':
        again = True
        print("Let's go again!")
    else:
        again = False
        print("Bye")

