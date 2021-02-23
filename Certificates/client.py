# Marwan Nour           marwan.nour@polytechnique.edu

import socket
import os
import string
import random
import sys

# Helper function for generating random strings
def get_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

# input: CA_pk, verify_output_file
if(len(sys.argv) != 3):
    print("Incorrect syntax")
    print("python3 client.py <CA_pk> <verify_output_file>")
    sys.exit(1)
    
CA_pk = sys.argv[1]
verify_output_file = sys.argv[2]

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 10001

############ GET FILE AND CERT FROM SERVER ############
server_original_file_contents = b''
server_cert_file_contents = b''
# Connect to server, receive file and cert
client_socket.connect((host, port))
server_original_file_contents = client_socket.recv(1024)
print("Received file")
print(server_original_file_contents)
# (optional) send ack
client_socket.send(b'ACK File')

# Write file to file
with open("clientfiles/server_original_file.txt", "wb") as f:
    f.write(server_original_file_contents)


server_cert_file_contents = client_socket.recv(1024)
print("Received cert")
print(server_cert_file_contents)
# (optional) send ack
client_socket.send(b'ACK Cert')

# Write cert to file
with open("clientfiles/server_cert_file.bin", "wb") as f:
    f.write(server_cert_file_contents)
    
############ VERIFY ############
os.system("openssl dgst -sha256 -verify " + CA_pk +  " -signature clientfiles/server_cert_file.bin < clientfiles/server_original_file.txt > clientfiles/" + verify_output_file)

verify_result = ''
with open("clientfiles/" + verify_output_file, "r") as f:
    verify_result = f.readlines()[0]

print(verify_result)

if(verify_result != 'Verified OK\n'):
    print("Verification failed")
    sys.exit(1)

# Extract server pk from file
server_pk = ''
with open("clientfiles/server_original_file.txt", "r") as f:
    server_pk = f.read()

server_pk = server_pk.split("\n", 1)[1] # Removes first line in the file (which is the identity)

server_pk = server_pk.encode()

# Write server pk to file
with open(os.getcwd() + "/clientfiles/server_pk.pem", "wb") as f:
    f.write(server_pk)

############ SEND ENCRYPTED KEY AND ENCRYPTED FILE TO SERVER ############
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

# Send encrypted key
client_socket.send(encrypted_sym_contents)
print("Sent encrypted sym file")
print(encrypted_sym_contents)

# (optional) recv ack
ack = client_socket.recv(1024)
print(ack)

# Encrypt file with symmetric key
print("ENCRYPTING FILE ...\n")
os.system("openssl enc -aes-256-cbc -base64 -pbkdf2 -k \"" + sym_key +  "\"< clientfiles/file_to_encrypt.txt > clientfiles/encrypted_file.bin")

# Read encrypted_file.bin into bytes variable
encrypted_file_contents = b''
with open(os.getcwd() + "/clientfiles/encrypted_file.bin", "rb") as f:
    encrypted_file_contents = f.read()

# Send encrypted file
client_socket.send(encrypted_file_contents)
print("Sent encrypted file")
print(encrypted_file_contents)

# (optional) recv ack
ack = client_socket.recv(1024)
print(ack)

# Close socket
client_socket.close()
