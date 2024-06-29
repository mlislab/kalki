import random

def diffie_hellman(p, g, private_key):
    public_key = pow(g, private_key, p)
    return public_key

def compute_shared_secret(public_key, private_key, p):
    shared_secret = pow(public_key, private_key, p)
    return shared_secret
p = 20
g = 5   


private_key_a = random.randint(1, p-1)
private_key_b = random.randint(1, p-1)
public_key_a = diffie_hellman(p, g, private_key_a)
public_key_b = diffie_hellman(p, g, private_key_b)

# Each party computes the shared secret
print(private_key_a)
print(private_key_b)
shared_secret_a = compute_shared_secret(public_key_b, private_key_a, p)
shared_secret_b = compute_shared_secret(public_key_a, private_key_b, p)

# Confirm that the shared secrets match
print(f"Shared secret (A): {shared_secret_a}")
print(f"Shared secret (B): {shared_secret_b}")

if shared_secret_a == shared_secret_b:
    print("Key exchange successful: Shared secrets match.")
else:
    print("Key exchange failed: Shared secrets do not match.")
