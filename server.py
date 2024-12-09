#This file contains the code that sets up a server to send the encrypted file
import socket

def server():
    #The ip address 127.0.0.1 ensures the server listens only on the local machine, making it accessible only from the same computer.
    host = '127.0.0.1'
    #65432 is a high port number chosen to avoid conflicts with other services.
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server listening on port", port)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            with open('file.txt.enc', 'rb') as f:
                conn.sendfile(f)

# Run the server
server()
