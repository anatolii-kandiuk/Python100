alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def caesar_cipher(input_text, shift, decode_or_encode):
    caesar_text = ""

    if decode_or_encode == "decode":
        shift *= -1
    
    for char in input_text:
        if char not in alphabet:
            caesar_text += char
            continue

        shifted_position = (alphabet.index(char) + shift) % len(alphabet)
        caesar_text += alphabet[shifted_position]

    return caesar_text

