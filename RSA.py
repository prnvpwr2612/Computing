import random

def is_prime(n, k=5):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for _ in range(k):
        x = pow(random.randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1: break
        else: return False
    return True

def generate_prime(bits):
    while True:
        n = random.getrandbits(bits)
        if is_prime(n): return n

def mod_inverse(a, m):
    def egcd(a, b):
        if a == 0: return (b, 0, 1)
        else: 
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    g, x, _ = egcd(a, m)
    if g != 1: raise Exception('Modular inverse does not exist')
    else: return x % m

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p-1) * (q-1)
    e = 65537  # Commonly used value for e
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    e, n = pk
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    d, n = pk
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Example usage
public_key, private_key = generate_keypair(1024)
message = "Hello, RSA!"
encrypted_msg = encrypt(public_key, message)
decrypted_msg = decrypt(private_key, encrypted_msg)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_msg}")
print(f"Decrypted message: {decrypted_msg}")