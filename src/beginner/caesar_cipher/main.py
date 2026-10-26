from caesar_cipher import caesar_cipher

exit = "no"

while exit == "no":
    decode_or_encode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    
    if decode_or_encode in ["encode", "decode"]:
        output_text = caesar_cipher(input_text, shift, decode_or_encode)
        print(output_text)
    else:
        print("Invalid input. Please enter 'encode' or 'decode'.")

    exit = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")