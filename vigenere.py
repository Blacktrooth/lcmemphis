import string
from helpers2 import alphabet_position, rotate_character

def encrypt(text, rot):
    alphabets = string.ascii_letters
    keystream = 0
    encrypted = ""
    rot.lower()
    for i in range(len(text)):
        keychar = keystream % len(rot)
        if text[i] in alphabets.lower():
            new_char = rotate_character(text[i], alphabet_position(rot[keychar]))
            new_char.lower()
            encrypted += new_char
            keystream += 1
        elif text[i] in alphabets.upper():
            new_char = rotate_character(text[i], alphabet_position(rot[keychar]))
            new_char.upper()
            encrypted += new_char
            keystream += 1            
        else:
            encrypted += text[i]
       
    return encrypted

def main():
    input_text = input("Type your sercret message: ")
    input_rot = input("Type your code word: ")

    print(encrypt(input_text, input_rot))

if __name__ == "__main__":
    main()