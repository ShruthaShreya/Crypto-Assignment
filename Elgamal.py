# Function to perform modular exponentiation
def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod
    return result

# Function to encrypt a message
def elgamal_encrypt(p, e1, e2, r, m):
    c1 = modular_exponentiation(e1, r, p)
    c2 = (m * modular_exponentiation(e2, r, p)) % p
    return c1, c2

# Function to decrypt a ciphertext
def elgamal_decrypt(p, c1, c2, d):
    # Compute the shared secret: c1^(p-1-d) mod p
    shared_secret = modular_exponentiation(c1, p - 1 - d, p)
    # Decrypt the message: m = (c2 * shared_secret) mod p
    m = (c2 * shared_secret) % p
    return m

# Example usage
if __name__ == "__main__":
    # Key generation
    p = 467  # A prime number
    e1 = 2   # A primitive root modulo p
    d = 127  # Private key (1 < d < p-1)
    e2 = modular_exponentiation(e1, d, p)  # Public key: e2 = e1^d mod p

    # Display the keys
    print(f"Public Key: (e1={e1}, e2={e2}, p={p})")
    print(f"Private Key: d={d}")

    # Encryption
    plaintext = 123  # Message to encrypt (numerical representation)
    r = 45  # Random integer (1 < r < p-1)
    c1, c2 = elgamal_encrypt(p, e1, e2, r, plaintext)
    print(f"Encrypted: c1={c1}, c2={c2}")

    # Decryption
    decrypted_message = elgamal_decrypt(p, c1, c2, d)
    print(f"Decrypted Message: {decrypted_message}")
