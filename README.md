# Encrypted-File-Transfer-System
This project demonstrates a practical approach to secure file handling, using RSA and AES encryption. Whether for personal use or as a learning exercise, this system showcases the principles of cryptography in action.

---

## Features
- **File Encryption:** AES encryption ensures fast and secure file encryption.
- **Key Management:** RSA encryption protects the AES key for secure sharing.
- **Secure Transmission:** Files are transmitted safely over a socket connection.
- **File Decryption:** Decrypts the received file using RSA and AES.

---

---

## Requirements
Install the required dependencies before running the scripts:
pip install cryptography

---

## Project Components

### 1. Key Generation (`generate_keys.py`)
Generates RSA key pairs for encryption and decryption:
- **Private Key:** Used for decrypting the AES key.
- **Public Key:** Used for encrypting the AES key.

#### Usage:
Run the following command to generate the keys:
python generate_keys.py

### Output files:
- **private_key.pem:** The private key (keep this secure!).
- **public_key.pem:** The public key for encrypting data.

---

### 2. File Encryption (encrypt.py)
This script encrypts a file by:
- Encrypting the file content using AES.
- Encrypting the AES key using the RSA public key.

#### Usage:
Prepare the file you want to encrypt (e.g., file.txt) and ensure public_key.pem is in the same directory. Then run:
python encrypt.py

---

### 3. File Decryption (decrypt.py)
Decrypts the encrypted file:
- The RSA private key decrypts the AES key.
- The AES key decrypts the file content.

#### Usage:
Ensure file.txt.enc and private_key.pem are in the same directory. Run:
python decrypt.py

---

### 4. Server (server.py)
This script sets up a server that:
- Listens for incoming connections.
- Sends the encrypted file to the connected client.

#### Usage:
Start the server on your machine. Run:
python server.py

---

### 5. Client (client.py)
The client connects to the server to receive the encrypted file.

#### Usage:
Run the client to fetch the file from the server:
python client.py





