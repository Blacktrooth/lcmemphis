import string

def alphabet_position(letter):

    alphabets = string.ascii_letters                              
    position = 0
    found = False
    if letter in alphabets.lower():                                                
        while position < len(alphabets.lower()) and not found:
            if alphabets.lower()[position] == letter:
                found = True                                                    
            else:
                position = position + 1
        if found:
            return position                                                     
    if letter in alphabets.upper():                                                
        while position < len(alphabets.upper()) and not found:
            if alphabets.upper()[position] == letter:
                found = True                                                    
            else:
                position = position + 1
        if found:
            return position                                                     

def rotate_character(char, rot):

    alphabets = string.ascii_letters                               
    char_pos = alphabet_position(char)
    if char in alphabets.lower():                                                  
        rotated = char_pos + rot
        if rotated >= 26:
            rotated = (char_pos + rot) % 26                                     
            return alphabets.lower()[rotated]                                      
        else:
            return alphabets.lower()[rotated]                                      

    elif char in alphabets.upper():                                               
        rotated = char_pos + rot
        if rotated >= 26:
            rotated = (char_pos + rot) % 26                                     
            return alphabets.upper()[rotated]                                     
                                              

    else:
        rotated = char
        return char            