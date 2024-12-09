# Encrypted-File-Transfer-System
This project demonstrates a practical approach to secure file handling, using RSA and AES encryption. Whether for personal use or as a learning exercise, this system showcases the principles of cryptography in action.

---

## Features
- **File Encryption:** AES encryption ensures fast and secure file encryption.
- **Key Management:** RSA encryption protects the AES key for secure sharing.
- **Secure Transmission:** Files are transmitted safely over a socket connection.
- **File Decryption:** Decrypts the received file using RSA and AES.

---

## Project Components

### 1. Key Generation (`generate_keys.py`)
Generates RSA key pairs for encryption and decryption:
- **Private Key:** Used for decrypting the AES key.
- **Public Key:** Used for encrypting the AES key.


