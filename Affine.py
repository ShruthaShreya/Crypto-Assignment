# Function to find modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# Function to encrypt the plaintext
def affine_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((a * (ord(char) - base) + b) % 26 + base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

# Function to decrypt the ciphertext
def affine_decrypt(ciphertext, a, b):
    decrypted_text = ""
    a_inv = mod_inverse(a, 26)  # Modular multiplicative inverse of 'a'
    if a_inv == -1:
        raise ValueError("Multiplicative inverse for 'a' does not exist. Choose a different value of 'a'.")
    
    for char in ciphertext:
        if char.isalpha():
            # Handle uppercase and lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((a_inv * (ord(char) - base - b)) % 26 + base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

# Example usage
if __name__ == "__main__":
    plaintext = "Hello World"
    a = 5  # 'a' must be coprime with 26
    b = 8  # Shift value

    print(f"Plaintext: {plaintext}")

    # Encryption
    ciphertext = affine_encrypt(plaintext, a, b)
    print(f"Encrypted Text: {ciphertext}")

    # Decryption
    decrypted_text = affine_decrypt(ciphertext, a, b)
    print(f"Decrypted Text: {decrypted_text}")
