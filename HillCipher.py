def text_to_numbers(text):
    return [ord(char.upper()) - ord('A') for char in text if char.isalpha()]


def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])


def matrix_multiply(matrix, vector, mod):
    result = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
        result[i] %= mod
    return result


def modular_inverse(value, mod):
    value = value % mod
    for x in range(1, mod):
        if (value * x) % mod == 1:
            return x
    raise ValueError("Inverse does not exist")


def matrix_inverse(matrix, mod):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    inv_det = modular_inverse(det, mod)

    matrix_inv = [
        [matrix[1][1] * inv_det % mod, -matrix[0][1] * inv_det % mod],
        [-matrix[1][0] * inv_det % mod, matrix[0][0] * inv_det % mod]
    ]

    # Adjust for negative values to fit in the range [0, mod)
    for i in range(2):
        for j in range(2):
            matrix_inv[i][j] = matrix_inv[i][j] % mod

    return matrix_inv


def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    n = len(key)
    plaintext = text_to_numbers(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), n):
        block = plaintext[i:i + n]
        if len(block) < n:  # Padding if needed
            block += [0] * (n - len(block))
        encrypted_block = matrix_multiply(key, block, 26)
        ciphertext += numbers_to_text(encrypted_block)

    return ciphertext


def decrypt(ciphertext, key):
    n = len(key)
    key_inv = matrix_inverse(key, 26)

    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = text_to_numbers(ciphertext[i:i + n])
        decrypted_block = matrix_multiply(key_inv, block, 26)
        plaintext += numbers_to_text(decrypted_block)

    # Remove any padding that was added during encryption
    plaintext = plaintext.rstrip('A')  # Assuming padding was done with 'A' which corresponds to 0

    return plaintext


# Example usage
name = "Reyone chaudhary"
key = [[3, 5], [7, 2]]  # Example key matrix

print(f"Full Name: {name}")
# Encryption
encrypted_name = encrypt(name, key)
print("Encrypted:", encrypted_name)

# Decryption
decrypted_name = decrypt(encrypted_name, key)
print("Decrypted:", decrypted_name)
