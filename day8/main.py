from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  output_text = ""    
  #if user chooses 'decode' we must shift backwards
  if cipher_direction == "decode":
    shift_amount *= -1
    
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      output_text += alphabet[new_position]
    else:
      output_text += char
  print(f"Here's the {cipher_direction}d result: {output_text}")

continue_cypher = True

while continue_cypher:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  #validate user input
  if direction == 'encode' or direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #if the user enters a shift that is greater than the number of letters in the alphabet:
    shift %= 26
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    continue_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    #validate user input
    if continue_or_no != 'yes':
        continue_cypher = False
        print("Goodbye.")
    else:
        continue_cypher = True
  else:
    continue_cypher = False
    print("Googbye!")