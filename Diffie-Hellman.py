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

def find_primitive_root(p):
    if p == 2: return 1
    p1 = 2
    p2 = (p-1) // p1
    while True:
        g = random.randint(2, p-1)
        if not (pow(g, (p-1)//p1, p) == 1) and not (pow(g, (p-1)//p2, p) == 1):
            return g

def diffie_hellman():
    p = generate_prime(64)
    g = find_primitive_root(p)
    
    print(f"Publicly shared prime: {p}")
    print(f"Publicly shared base: {g}")
    
    a_private = random.randint(1, p-1)
    a_public = pow(g, a_private, p)
    
    b_private = random.randint(1, p-1)
    b_public = pow(g, b_private, p)
    
    print(f"Alice's public key: {a_public}")
    print(f"Bob's public key: {b_public}")
    
    a_shared_secret = pow(b_public, a_private, p)
    b_shared_secret = pow(a_public, b_private, p)
    
    print(f"Alice's computed shared secret: {a_shared_secret}")
    print(f"Bob's computed shared secret: {b_shared_secret}")
    
    assert a_shared_secret == b_shared_secret, "The shared secrets should be equal"

diffie_hellman()