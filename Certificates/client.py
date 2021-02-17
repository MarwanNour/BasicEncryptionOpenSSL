# Marwan Nour           marwan.nour@polytechnique.edu

import socket
import os
import string
import random
import cert_verify

# Helper function for generating random strings
def get_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 10001

server_pk = b''

############ GET PUBLIC KEY FROM SERVER ############
# Connect to server, receive pk
with client_socket as s:
    s.connect((host, port))
    server_pk = s.recv(1024)

print("Received: ", repr(server_pk))

# Write server pk to file
with open(os.getcwd() + "/clientfiles/server_pk.pem", "wb") as f:
    f.write(server_pk)

# Generate random symmetric key
sym_key = get_random_string(8)
print("Random Sym Key : " + (str)(sym_key))

# Write symmetric key to file
with open(os.getcwd() + "/clientfiles/sym_key.txt", "wb") as f:
    f.write(sym_key.encode())

# Encrypt symmetric key with pk
print("ENCRYPTING SYM KEY...\n")
os.system("openssl rsautl -encrypt -pubin -inkey clientfiles/server_pk.pem < clientfiles/sym_key.txt > clientfiles/encrypted_sym.txt")

# Read encrypted_sym.txt into bytes variable
encrypted_sym_contents = b''
with open(os.getcwd() + "/clientfiles/encrypted_sym.txt", "rb") as f:
    encrypted_sym_contents = f.read()


# Encrypt file with symmetric key
print("ENCRYPTING FILE ...\n")
os.system("openssl enc -aes-256-cbc -base64 -pbkdf2 -k \"" + sym_key +  "\"< clientfiles/file_to_encrypt.txt > clientfiles/encrypted_file.bin")

# Read encrypted_file.bin into bytes variable
encrypted_file_contents = b''
with open(os.getcwd() + "/clientfiles/encrypted_file.bin", "rb") as f:
    encrypted_file_contents = f.read()

############ SEND ENCRYPTED KEY AND ENCRYPTED FILE TO SERVER ############
# Connect to server, Send encrypted key
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with client_socket as s:
    s.connect((host, port))
    s.sendall(encrypted_sym_contents)

# Connect to server, Send encrypted file
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with client_socket as s:
    s.connect((host, port))
    s.sendall(encrypted_file_contents)
