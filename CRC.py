# Function to perform XOR operation on two binary strings
def xor(a, b):
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

# Function to perform Modulo-2 division
def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time.
    pick = len(divisor)
    
    # Slicing the dividend to appropriate length for the first step
    tmp = dividend[0: pick]
    
    # Continue until we have processed all bits
    while pick < len(dividend):
        # If the first bit is 1, perform XOR with the divisor
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:  # If the first bit is 0, perform XOR with a string of 0s
            tmp = xor('0'*pick, tmp) + dividend[pick]
        
        # Move to the next bit of the dividend
        pick += 1
    
    # For the last n bits, carry out the division normally
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    
    # Return the remainder after division
    return tmp

# Function to encode data by appending the remainder to the data
def encodeData(data, key):
    l_key = len(key)
    
    # Append (length of key - 1) zeros to the end of the data
    appended_data = data + '0' * (l_key - 1)
    
    # Find the remainder after division
    remainder = mod2div(appended_data, key)
    
    # The codeword is the original data plus the remainder
    codeword = data + remainder
    
    print("Remainder:", remainder)
    print("Encoded Data (Data + Remainder):", codeword)

# Driver code
data = "100100"
key = "1101"
encodeData(data, key)