# This file contains the code that generates both the private and public key
from cryptography.hazmat.primitives.asymmetric import rsa # type: ignore
from cryptography.hazmat.primitives import serialization # type: ignore

print("Generating RSA keys...")
# Generate RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Save the private key to a file
# the private key will be saved in the "private_key.pem" file, you can change the file name to your liking.
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Generate RSA public key
public_key = private_key.public_key()

# Save the public key to a file
# the public key will be saved in the "public_key.pem" file, you can change the file name to your liking.
with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("RSA keys generated successfully.")
