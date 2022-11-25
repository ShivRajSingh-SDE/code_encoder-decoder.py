alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_number):
  cipher_text = ""
  for latter in plain_text:
    possition=alphabet.index(latter)
    new_posstion= possition+ shift_number
    new_letter = alphabet[new_posstion]
    cipher_text += new_letter
    print(f"your new encoded text is {cipher_text}")


def decrypt(cipher_text, shift_number):
  plain_text = ""
  for latter in cipher_text:
    possition=alphabet.index(latter)
    new_posstion= possition- shift_number
    new_letter = alphabet[new_posstion]
    plain_text += new_letter
    print(f"your new encoded text is {plain_text}")    
    
    

if direction == "encode":
  encrypt(plain_text= text, shift_number= shift )
elif direction == "decode":
  decrypt(cipher_text=text, shift_number= shift)
