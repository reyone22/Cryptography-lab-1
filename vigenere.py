def generate_key(plaintext, key):
    # Repeat the key to match the length of the plaintext
    key = list(key)
    if len(plaintext) == len(key):
        return ''.join(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = generate_key(plaintext, key).upper()
    ciphertext = []

    for i in range(len(plaintext)):
        # Shift the plaintext character by the key character
        x = (ord(plaintext[i]) + ord(key[i])) % 26
        x += ord('A')
        ciphertext.append(chr(x))

    return ''.join(ciphertext)

def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    key = generate_key(ciphertext, key).upper()
    plaintext = []

    for i in range(len(ciphertext)):
        # Reverse the shift by the key character
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plaintext.append(chr(x))

    return ''.join(plaintext)

# Example usage
plaintext = "Reyone Chaudhary"
key = "KEY"
print(f"Plaintext: {plaintext}")
# Encryption
encrypted_text = encrypt_vigenere(plaintext, key)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Decrypted:", decrypted_text)
