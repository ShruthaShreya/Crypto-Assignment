# Function to repeat the key to match the length of the plaintext
def repeat_key(text, key):
    key = key.upper()
    repeated_key = ""
    key_index = 0

    for char in text:
        if char.isalpha():  # Only repeat key for alphabetic characters
            repeated_key += key[key_index % len(key)]
            key_index += 1
        else:
            repeated_key += char  # Keep non-alphabetic characters as is
    return repeated_key

# Function to encrypt plaintext using the Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    key = repeat_key(plaintext, key)
    encrypted_text = ""

    for p_char, k_char in zip(plaintext, key):
        if p_char.isalpha():
            base = ord('A') if p_char.isupper() else ord('a')
            k_base = ord('A')  # Key is always uppercase
            encrypted_char = chr((ord(p_char) - base + (ord(k_char) - k_base)) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += p_char  # Non-alphabetic characters remain unchanged

    return encrypted_text

# Function to decrypt ciphertext using the Vigenère Cipher
def vigenere_decrypt(ciphertext, key):
    key = repeat_key(ciphertext, key)
    decrypted_text = ""

    for c_char, k_char in zip(ciphertext, key):
        if c_char.isalpha():
            base = ord('A') if c_char.isupper() else ord('a')
            k_base = ord('A')  # Key is always uppercase
            decrypted_char = chr((ord(c_char) - base - (ord(k_char) - k_base)) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += c_char  # Non-alphabetic characters remain unchanged

    return decrypted_text

# Example usage
if __name__ == "__main__":
    plaintext = "Hello World"
    key = "KEY"

    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")

    # Encryption
    ciphertext = vigenere_encrypt(plaintext, key)
    print(f"Encrypted Text: {ciphertext}")

    # Decryption
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")
