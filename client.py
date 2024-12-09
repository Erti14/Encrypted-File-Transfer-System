#This file contains the code that sets up a client to receive the encrypted file
import socket

def client():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open('received_file.enc', 'wb') as f:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                f.write(data)

    print("File received successfully.")

# Run the client
client()

