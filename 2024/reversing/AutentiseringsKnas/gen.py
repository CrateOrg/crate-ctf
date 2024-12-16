from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=768,
    backend=default_backend()
)

# Extract components
private_numbers = private_key.private_numbers()
public_numbers = private_numbers.public_numbers
modulus = public_numbers.n
private_exponent = private_numbers.d
public_exponent = public_numbers.e

# Output components in base 10
print(f"Modulus (n) in base 10: {modulus}")
print(f"Private Exponent (d) in base 10: {private_exponent}")
print(f"Public Exponent (e) in base 10: {public_exponent}")

