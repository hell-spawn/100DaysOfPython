alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    chiper_text = "" 
    for letter in text:
        index = (alphabet.index(letter) + shift) if (alphabet.index(letter) + shift) < len(alphabet) else alphabet.index(letter) + shift - len(alphabet)
        chiper_text += alphabet[index]
    print(f"The encoded text is {chiper_text}")

def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        index = (alphabet.index(letter) - shift) if (alphabet.index(letter) - shift) > -1 else alphabet.index(letter) - shift + len(alphabet)
        plain_text += alphabet[index]
    print(f"The decoded text is {plain_text}")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for char in start_text:
      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. start_text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      if char in alphabet:
        position = alphabet_2.index(char)
        new_position = position + shift_amount
        end_text += alphabet_2[new_position]
      else:
        end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# caesar(text, shift, direction)

if direction == "encode":
    encrypt(text, shift)

if direction == "decode":
    decrypt(text, shift)
