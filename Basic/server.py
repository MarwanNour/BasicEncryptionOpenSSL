# Marwan Nour           marwan.nour@polytechnique.edu

import socket
import os

# Use openssl to generate the keys
os.system("openssl genrsa -out serverfiles/private.pem 2048")
os.system("openssl rsa -in serverfiles/private.pem -pubout -out serverfiles/public.pem")

# Read pk file into bytes variable
pubfile_contents = b''
with open(os.getcwd() + "/serverfiles/public.pem", "rb") as f:
    pubfile_contents = f.read()

print(pubfile_contents)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 10001

############ SEND PUBLIC KEY TO CLIENT ############
# Bind
server_socket.bind((host, port))
# Listen
server_socket.listen()
# Accept
while True:
    conn, addr = server_socket.accept()
    print("Connection from: ", addr)
    conn.send(pubfile_contents)
    print("Sent public key")

    ############ GET ENCRYPTED SYM KEY AND ENCRYPTED FILE FROM CLIENT############
    encrypted_sym = conn.recv(1024)
    print("Received Encrypted Sym Key")
    print(encrypted_sym)

    # (optional) send ack
    conn.send(b'ACK Sym key')

    # Write encrypted sym key to file
    with open(os.getcwd() + "/serverfiles/encrypted_sym.txt", "wb") as f:
        f.write(encrypted_sym)


    encrypted_file = conn.recv(1024)
    print("Received Encrypted File")
    print(encrypted_file)

    # (optional) send ack
    conn.send(b'ACK Enc file')
    
    # Write encrypted file to file
    with open(os.getcwd() + "/serverfiles/encrypted_file.bin", "wb") as f:
        f.write(encrypted_file)

    ############ DECRYPT ############
    print("DECRYPTING ...\n")
    # Decrypt encrypted sym key with sk
    os.system("openssl rsautl -decrypt -inkey serverfiles/private.pem < serverfiles/encrypted_sym.txt > serverfiles/decrypted_sym.txt")

    # Read decrypted sym key into variable
    decrypted_sym_key = b''
    with open(os.getcwd() + "/serverfiles/decrypted_sym.txt", "rb") as f:
        decrypted_sym_key = f.read()

    print(decrypted_sym_key.decode())

    # Decrypt encrypted file with decrypted sym
    os.system("openssl enc -d -aes-256-cbc -base64 -pbkdf2 -k " + (str)(decrypted_sym_key.decode()) + " < serverfiles/encrypted_file.bin > serverfiles/decrypted_file.txt")
