def shift_character(char: str, shift: int) -> str:
    """Shift a single character by number of positions. 'shift' determines the amount of of places a character is shifted """
   
    #check if character is an alphabet
    if char.isalpha():
        """Choose the starting point based on the character's case, check if lowercase, otherwise the character uppercase
            this determines the starting value in ASCII code, lowercase a - z = (97 - 122), uppercase A - Z = (65 - 90) """
        start = ord('a') if char.islower() else ord('A')
        # shift character and make sure it wraps around the range of the alphabet in ASCII code
        shifted_char = chr((ord(char) - start + shift) % 26 + start)
        return shifted_char
    # Return the original character if it's not an alphabet letter
    return char


def encrypt(text, shift):
    """Encrypts the text by applying a caesar cipher shift to each letter"""
    encrypted_text = ''.join(shift_character(char, shift) for char in text)
    return encrypted_text


def decrypt(text, shift):
    """Decrypts by reversing the shift on each letter"""
    decrypted_text = ''.join(shift_character(char, -shift) for char in text)
    return decrypted_text

def brute_force(text):
    """Return a list of all possible decrpytions, each iteration outputs the shift number 
    and the decrypted text that corresponds to the shift number. Add the shift value and 
    decrypted text to the decryption_results list"""
    # create an empty list to store decrpytion results
    decryption_results = []
    # Attempt all possible shifts (0 - 25) in loop
    for shift in range(26):
        decrypted_text = decrypt(text, shift)
        decryption_results.append((shift,decrypted_text))
    
    return decryption_results




