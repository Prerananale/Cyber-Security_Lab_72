import math

# Given prime numbers
p = 23
q = 19

# Calculate n
n = p * q
print("n =", n)

# Calculate Euler's totient function
phi = (p - 1) * (q - 1)

# Choose a value for the public exponent
e = 17
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

print("e =", e)

# Calculate the private exponent using modular multiplicative inverse
d = pow(e, -1, phi)
print("d =", d)

# Validate public and private keys
if 1 < e < phi and math.gcd(e, phi) == 1:
    # Generate public and private keys
    public_key = (e, n)
    private_key = (d, n)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Encrypt plaintext
    def encrypt(plaintext, public_key):
        e, n = public_key
        return pow(plaintext, e, n)

    # Decrypt ciphertext
    def decrypt(ciphertext, private_key):
        d, n = private_key
        return pow(ciphertext, d, n)

    plaintext = 88 
    ciphertext = encrypt(plaintext, public_key)
    decrypted_text = decrypt(ciphertext, private_key)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text)
else:
    print("Invalid public key. Please try again.")
