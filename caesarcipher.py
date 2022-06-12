

from tkinter.messagebox import YES

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encrpt function 
def encrypt(text, shift):
    if shift > 26:
        shift %= 26

    cipher_text = ""
    tem = 0
    for char  in text:
      if char in alphabet:
            k = alphabet.index(char)
            if(k+shift) >= 25:
                  tem = k+shift-26
                  cipher_text += alphabet[tem]
            else:
                  cipher_text += alphabet[k+shift]
      else:
            cipher_text+=char
            
      
    print(f"The encoded text is:{cipher_text}")

#decrypt function 
def decrypt(text, shift):
    if shift > 26:
        shift %= 26
    decrypt_txet = ""
    tem = 0
    for char  in text:
      if char in alphabet:
            k = alphabet.index(char)
            if k-shift < 0:
                  tem = k+26-shift
                  decrypt_txet += alphabet[tem]
            else:
                  decrypt_txet += alphabet[k-shift]
      else:
         decrypt_txet+=char   
    print(f"The decoded text is:{decrypt_txet}")


x = YES
while x == YES:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      if direction.isalpha()==False:
           
            direction = input("please type  'encode' to encrypt, type 'decode' to decrypt:\n")
      text = input("Type your message:\n").lower()
      
      shift = int(input("Type the shift number:\n"))
      
            




      if direction.lower() == "encode":
            encrypt(text, shift)
      elif direction.lower() == "decode":
            decrypt(text, shift)
      x=input("type yes for continue or no to end:")
      
            
