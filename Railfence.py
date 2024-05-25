def encrypt_rail_fence(text, key):
    rail = [''] * key
    direction = 1
    row = 0

    for char in text:
        rail[row] += char
        row += direction

        if row == key - 1 or row == 0:
            direction *= -1

    return ''.join(rail)

def decrypt_rail_fence(text, key):
    rail = [''] * key
    direction = 1
    row = 0

    # Pre-fill rail with placeholders
    for i in range(len(text)):
        rail.append('')

    # Mark the positions of the characters in the rail pattern
    for i in range(len(text)):
        rail[row] += '*'
        row += direction

        if row == key - 1 or row == 0:
            direction *= -1

    # Replace placeholders with characters from the text
    index = 0
    for i in range(len(rail)):  # Iterate over the whole rail
        for j in range(len(text)):  # Iterate over the length of the text
            if j < len(rail[i]):  # Check if the index is within the range of the current row
                if rail[i][j] == '*':
                    rail[i] = rail[i][:j] + text[index] + rail[i][j+1:]
                    index += 1

    # Combine rows to form the decrypted text
    decrypted_text = ''
    direction = 1
    row = 0

    for i in range(len(text)):
        decrypted_text += rail[row][0]
        rail[row] = rail[row][1:]
        row += direction

        if row == key - 1 or row == 0:
            direction *= -1

    return decrypted_text

# Example usage
full_name = "Reyone chaudhary"
key = 3

print(f"Full Name: {full_name}")
# Encryption
encrypted_name = encrypt_rail_fence(full_name, key)
print("Encrypted:", encrypted_name)

# Decryption
decrypted_name = decrypt_rail_fence(encrypted_name, key)
print("Decrypted:", decrypted_name)
