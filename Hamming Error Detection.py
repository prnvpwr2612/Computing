def calculate_parity_bits(data):
    m = len(data)
    r = 0
    while (2**r < m + r + 1):
        r += 1
    parity_bits = [0] * r
    codeword = []
    j = 0
    for i in range(1, m + r + 1):
        if 2**j == i:
            codeword.append(0)
            j += 1
        else:
            codeword.append(int(data[i - j - 1]))

    for i in range(r):
        parity_index = 2**i
        parity_bits[i] = sum(codeword[j] for j in range(parity_index - 1, m + r, parity_index * 2)) % 2
        codeword[parity_index - 1] = parity_bits[i]

    return ''.join(map(str, codeword))

def decode_hamming(codeword):
    r = 0
    m = len(codeword) - 1
    while (2**r < m + 1):
        r += 1

    parity_indices = [2**i for i in range(r)]
    error_pos = 0

    for i in parity_indices:
        parity_check = sum(int(codeword[j]) for j in range(i - 1, len(codeword), i * 2)) % 2
        if parity_check != 0:
            error_pos += i

    if error_pos != 0:
        codeword = list(codeword)
        codeword[error_pos - 1] = '0' if codeword[error_pos - 1] == '1' else '1'
        return ''.join(codeword), error_pos
    return codeword, None

data = "1011"
codeword = calculate_parity_bits(data)
print("Encoded Codeword:", codeword)

correct_codeword = codeword
wrong_codeword = codeword[:2] + ('1' if codeword[2] == '0' else '0') + codeword[3:]

decoded_correct, error_pos_correct = decode_hamming(correct_codeword)
decoded_wrong, error_pos_wrong = decode_hamming(wrong_codeword)

print("Decoded Correct Codeword:", decoded_correct, "Error Position:", error_pos_correct)
print("Decoded Wrong Codeword:", decoded_wrong, "Error Position:", error_pos_wrong)