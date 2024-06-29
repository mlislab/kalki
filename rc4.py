def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key, text):
    S = KSA([ord(c) for c in key])
    print(S)
    keystream = PRGA(S)
    return ''.join([chr(ord(c) ^ next(keystream)) for c in text])

# Example usage
key = "lok"
plaintext = "lokeshwar"
ciphertext = RC4(key, plaintext)
decrypted_text = RC4(key, ciphertext)
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
