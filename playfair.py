def generate_playfair_matrix(key):
    key = ''.join(sorted(set(key.upper().replace('J', 'I')), key=lambda x: key.index(x)))
    matrix = [[0] * 5 for _ in range(5)]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    used = set()
    idx = 0

    for char in key:
        if char not in used:
            matrix[idx // 5][idx % 5] = char
            used.add(char)
            idx += 1

    for char in alphabet:
        if char not in used:
            matrix[idx // 5][idx % 5] = char
            used.add(char)
            idx += 1

    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair_encrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_decrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(" ", "")
    prepared_text = ""

    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
            if char1 == char2:
                prepared_text += char1 + 'X'
                i += 1
            else:
                prepared_text += char1 + char2
                i += 2
        else:
            prepared_text += char1 + 'X'
            i += 1

    return prepared_text

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    prepared_text = prepare_text(text)
    encrypted_text = ""

    for i in range(0, len(prepared_text), 2):
        encrypted_text += playfair_encrypt_pair(matrix, prepared_text[i:i + 2])

    return encrypted_text

def playfair_decrypt(encrypted_text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""

    for i in range(0, len(encrypted_text), 2):
        decrypted_text += playfair_decrypt_pair(matrix, encrypted_text[i:i + 2])

    return decrypted_text

full_name = "Reyone chaudhary"
key = "KEYWORD"

encrypted = playfair_encrypt(full_name, key)
decrypted = playfair_decrypt(encrypted, key)
print("Plaintext:",full_name)
print("Playfair Cipher Encryption:", encrypted)
print("Playfair Cipher Decryption:", decrypted)
