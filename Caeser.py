def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text


if __name__ == '__main__':
    full_name = "Reyone Chaudhary"
    shift = 2
    encrypted_name = encrypt(full_name, shift)
    decrypted_name = decrypt(encrypted_name, shift)
    print(f"Original name : {full_name}")
    print(f'Encrypted text : {encrypted_name}')
    print(f'Decrypted text : {decrypted_name}')
