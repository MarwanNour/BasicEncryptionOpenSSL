# Marwan Nour           marwan.nour@polytechnique.edu

import socket
import os
import sys

# input: original file, cert_file
if(len(sys.argv) != 3):
    print("Incorrect syntax")
    print("python3 server.py <original_file> <cert_file>")
    sys.exit(1)

original_file = sys.argv[1]
cert_file = sys.argv[2]

# print(original_file)
# print(cert_file)

if (not os.path.isfile(original_file)):
    print("Original file doesn't exist")
    sys.exit(1)

if (not os.path.isfile(cert_file)):
    print("Certificate file doesn't exist")
    sys.exit(1)


# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 10001

############ SEND FILE AND CERTIFICATE TO CLIENT ############
# Read file into bytes variable
original_file_contents = b''
with open(original_file, "rb") as f:
    original_file_contents = f.read()

# print(original_file_contents)

# Read cert into bytes variable
cert_file_contents = b''
with open(cert_file, "rb") as f:
    cert_file_contents = f.read()

# print(cert_file_contents)

# Bind
server_socket.bind((host, port))
# Listen
server_socket.listen()
# Accept
while True:
    conn, addr = server_socket.accept()
    print("Connection from: ", addr)
    # Send file
    conn.send(original_file_contents)
    print("Sent original file")
    print(original_file_contents)
    # (optional) Receive ACK 
    ack = conn.recv(1024)
    print(ack)
    # Send cert
    conn.send(cert_file_contents)
    print("Sent cert file")
    print(cert_file_contents)
    # (optional) Receive ACK 
    ack = conn.recv(1024)
    print(ack)

    ############ GET ENCRYPTED SYM KEY AND ENCRYPTED FILE FROM CLIENT############
    encrypted_sym = conn.recv(1024)
    print("Received Encrypted Sym Key")
    print(encrypted_sym)
    conn.send(b'ACK Sym key')

    # Write encrypted sym key to file
    with open(os.getcwd() + "/serverfiles/encrypted_sym.txt", "wb") as f:
        f.write(encrypted_sym)

    encrypted_file = conn.recv(1024)
    print("Received Encrypted File")
    print(encrypted_file)
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
