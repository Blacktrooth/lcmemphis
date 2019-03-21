from helpers2 import alphabet_position, rotate_character

def encrypt(text, rot):
    new_text = ""
    for char in text:
        new_char = rotate_character(char, rot)
        new_text += str(new_char)

    return new_text

def main():
    input_text = input("Type your message: ")
    input_rot = int(input("Rotate by: "))

    print(encrypt(input_text, input_rot))

if __name__ == "__main__":
    main()