import hashlib
text = b'Hello, world!' 
hash_value = hashlib.sha512(text).hexdigest()
print(hash_value)