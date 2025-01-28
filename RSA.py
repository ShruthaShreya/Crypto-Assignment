# Extended Euclidean Algorithm to find modular inverse
def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Function to find modular inverse
def mod_inverse(e, phi):
    gcd, x, _ = extended_euclidean(e, phi)
    if gcd != 1:
        raise ValueError("No modular inverse exists for the given e and phi.")
    return x % phi

# Function to encrypt a plaintext message
def rsa_encrypt(plaintext, e, n):
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Function to decrypt a ciphertext
def rsa_decrypt(ciphertext, d, n):
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_text

# RSA Key Generation and Encryption/Decryption Example
if __name__ == "__main__":
    # Step 1: Select two prime numbers (small for simplicity)
    p = 61
    q = 53
    n = p * q  # Compute n
    phi = (p - 1) * (q - 1)  # Compute Euler's Totient Function

    # Step 2: Choose public key 'e'
    e = 17  # e must be coprime with phi
    if extended_euclidean(e, phi)[0] != 1:
        raise ValueError("'e' is not coprime with phi. Choose a different 'e'.")

    # Step 3: Compute private key 'd'
    d = mod_inverse(e, phi)

    # Display keys
    print(f"Public Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")

    # Step 4: Encrypt and decrypt a word
    plaintext = "HELLO"
    print(f"Plaintext: {plaintext}")

    # Encryption
    ciphertext = rsa_encrypt(plaintext, e, n)
    print(f"Encrypted Text: {ciphertext}")

    # Decryption
    decrypted_text = rsa_decrypt(ciphertext, d, n)
    print(f"Decrypted Text: {decrypted_text}")
