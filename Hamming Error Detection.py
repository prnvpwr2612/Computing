def hamming_encode(data):
    m = len(data)
    r = 0
    while 2**r < m + r + 1:
        r += 1
    
    encoded = ['0'] * (m + r)
    j = 0
    for i in range(1, m + r + 1):
        if i & (i - 1) != 0:
            encoded[i-1] = data[j]
            j += 1
    
    for i in range(r):
        parity = 0
        for j in range(1, m + r + 1):
            if j & (1 << i):
                parity ^= int(encoded[j-1])
        encoded[2**i - 1] = str(parity)
    
    return ''.join(encoded)

def hamming_decode(encoded):
    n = len(encoded)
    r = 0
    while 2**r < n:
        r += 1
    
    error = 0
    for i in range(r):
        parity = 0
        for j in range(1, n + 1):
            if j & (1 << i):
                parity ^= int(encoded[j-1])
        if parity != 0:
            error += 2**i
    
    if error != 0:
        encoded = list(encoded)
        encoded[error-1] = str(1 - int(encoded[error-1]))
        encoded = ''.join(encoded)
    
    decoded = ''
    j = 0
    for i in range(1, n + 1):
        if i & (i - 1) != 0:
            decoded += encoded[i-1]
    
    return decoded

# Example usage
data = "1011001"
encoded = hamming_encode(data)
print(f"Original data: {data}")
print(f"Hamming encoded: {encoded}")
print(f"Hamming decoded: {hamming_decode(encoded)}")