#This file contains the code that decrypts the file using the RSA private key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes # type: ignore
from cryptography.hazmat.primitives import padding # type: ignore
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding # type: ignore
from cryptography.hazmat.primitives import hashes # type: ignore
from cryptography.hazmat.backends import default_backend # type: ignore
from cryptography.hazmat.primitives import serialization # type: ignore

def decrypt_file(encrypted_file_path, private_key_path):
    # Read the private key
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

    # Read the encrypted data
    with open(encrypted_file_path, 'rb') as f:
        encrypted_aes_key = f.read(256)  # RSA key size is 2048 bits (256 bytes)
        iv = f.read(16)  # Read the IV
        encrypted_data = f.read()

    # Decrypt the AES key with the RSA private key
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Create a cipher object
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Write the decrypted data to a new file
    with open(encrypted_file_path[:-4], 'wb') as f:
        f.write(data)

    print(f"File {encrypted_file_path} decrypted successfully.")

# Example usage
decrypt_file('received_file.enc', 'private_key.pem')
