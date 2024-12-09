#This file contains the code that  encrypts a file using AES and encrypts the AES key with the RSA public key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes # type: ignore
from cryptography.hazmat.primitives import padding # type: ignore
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding # type: ignore
from cryptography.hazmat.primitives import hashes # type: ignore
from cryptography.hazmat.backends import default_backend # type: ignore
from cryptography.hazmat.primitives import serialization # type: ignore
import os

def encrypt_file(file_path, public_key_path):
    # Generate a random AES key
    aes_key = os.urandom(32)

    # Read the public key
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())

    # Encrypt the AES key with the RSA public key
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Read the file data
    with open(file_path, 'rb') as f:
        data = f.read()

    # Pad the data
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create a cipher object
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted AES key, IV, and encrypted data to a new file
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted_aes_key + iv + encrypted_data)

    print(f"File {file_path} encrypted successfully.")

# Example usage
# The file with the name "file.txt" will be encrypted with the key "public.key.pem"
encrypt_file('file.txt', 'public_key.pem')
