def generate_key(text,key):
    key = list(key)
    if(len(text)==len(key)):
        return key
    else:
        for i in range(len(text)-len(key)):
            key.append(key[i%len(key)])
    return "".join(key)
def encrypt(text,key):
    key = generate_key(text,key)
    cipher = []
    for i in range(len(text)):
        x = (ord(text[i])+ord(key[i]))%26
        x += ord('A')
        cipher.append(chr(x))
    return "".join(cipher)

def decrypt(cipher_text,key):
    key = generate_key(cipher_text,key)
    original = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i])-ord(key[i]) + 26)%26
        x += ord('A')
        original.append(chr(x))
    return "".join(original)

text = "HELLO"
key = "KEY"
cipher_text = encrypt(text,key)
print(cipher_text)
print(decrypt(cipher_text,key))