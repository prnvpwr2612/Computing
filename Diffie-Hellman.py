import random

def generate_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return random.choice(primes)

def generate_primitive_root(prime):
    for g in range(2, prime):
        if pow(g, prime - 1, prime) == 1:
            return g
    return None

def generate_private_key(prime):
    return random.randint(2, prime - 2)

def calculate_public_key(prime, g, private_key):
    return pow(g, private_key, prime)

def calculate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)

def encrypt_message(message, shared_secret):
    return ''.join([chr(ord(c) ^ shared_secret) for c in message])

def decrypt_message(encrypted_message, shared_secret):
    return ''.join([chr(ord(c) ^ shared_secret) for c in encrypted_message])

p = generate_prime()
g = generate_primitive_root(p)
print("Shared Parameters:")
print("Prime (p):", p)
print("Primitive root (g):", g)

jenish_private = generate_private_key(p)
jenish_public = calculate_public_key(p, g, jenish_private)
arnold_private = generate_private_key(p)
arnold_public = calculate_public_key(p, g, arnold_private)

print("\nJenish's keys:")
print("Private key:", jenish_private)
print("Public key:", jenish_public)

print("\nArnold's keys:")
print("Private key:", arnold_private)
print("Public key:", arnold_public)

jenish_shared_secret = calculate_shared_secret(p, arnold_public, jenish_private)
arnold_shared_secret = calculate_shared_secret(p, jenish_public, arnold_private)

print("\nShared Secrets:")
print("Jenish's calculated shared secret:", jenish_shared_secret)
print("Arnold's calculated shared secret:", arnold_shared_secret)

if jenish_shared_secret == arnold_shared_secret:
    print("\nKey exchange successful! Both parties have the same shared secret.")
else:
    print("\nKey exchange failed. The shared secrets do not match.")

sender = "Jenish"
receiver = "Arnold"
original_message = "Hello Arnold, this is a secret message from Jenish!"
print("\nScenario 1: (sender) sends a message to (receiver)")
print("Original message:", original_message)
encrypted_message = encrypt_message(original_message, jenish_shared_secret)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt_message(encrypted_message, arnold_shared_secret)
print("Decrypted message:", decrypted_message)

print("\n" + "-" * 50 + "\n")

sender = "Arnold"
receiver = "Jenish"
original_message = "Hi Jenish, I received your message. Here's my reply!"
print("Scenario 2: (sender) sends a message to (receiver)")
print("Original message:", original_message)
encrypted_message = encrypt_message(original_message, arnold_shared_secret)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt_message(encrypted_message, jenish_shared_secret)
print("Decrypted message:", decrypted_message)