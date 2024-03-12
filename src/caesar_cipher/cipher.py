def shift_character(char: str, shift: int) -> str:
    """Shift a single character by a given number of positions."""
    if char.isalpha():
        # Choose the starting point based on the character's case
        start = ord('a') if char.islower() else ord('A')

        # Calculate the shifted characters
        shifted_char = chr((ord(char) - start + shift) % 26 + start)
        return shifted_char
    # Return the original character if it's not a letter
    return char


def encrypt(text, shift):
    """Encrypts the text by applying a caesar shift"""
    encrypted_text = ''.join(shift_character(char, shift) for char in text)
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ''.join(shift_character(char, -shift) for char in text)
    return decrypted_text

def brute_force(text):
    """Return a list of all possible decrpytions, each with the shift used."""
    return [{"shift": shift, "decrypted": decrypt(text, shift)} for shift in range(26)]

