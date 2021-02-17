# Marwan Nour           marwan.nour@polytechnique.edu

import socket
import os
import sys

# input: identity, cert_file
if(len(sys.argv) != 3):
    print("Incorrect syntax")
    print("python3 server.py <identity> <cert_file>")
    sys.exit(1)

identity = sys.argv[1]
cert_file = sys.argv[2]

print(identity)
print(cert_file)

if (not os.path.isfile(os.getcwd() + "/serverfiles/" + cert_file)):
    print("Certificate file doesn't exist")
    sys.exit(1)

# Use openssl to generate the keys
os.system("openssl genrsa -out serverfiles/private.pem 2048")
os.system("openssl rsa -in serverfiles/private.pem -pubout -out serverfiles/public.pem")

# Read pk file into string variable
pubfile_contents = ''
with open(os.getcwd() + "/serverfiles/public.pem", "r") as f:
    pubfile_contents = f.read()

print(pubfile_contents)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 10001

############ SEND FILE AND CERTIFICATE TO CLIENT ############

# Read file into bytes variable
original_file_contents = b''
with open(os.getcwd() + "/serverfiles/" + identity + "_file_to_sign.txt", "rb") as f:
    original_file_contents = f.read()

# Read cert into bytes variable
cert_file_contents = b''
with open(os.getcwd() + "/serverfiles/" + cert_file, "rb") as f:
    cert_file_contents = f.read()

# Bind
server_socket.bind((host, port))
# Listen
server_socket.listen(5)
# Accept
conn, addr = server_socket.accept()
with conn:
    print("Connection from: ", addr)
    conn.sendall(original_file_contents)
    print("Sent original file")

# Listen
server_socket.listen(5)
# Accept
conn, addr = server_socket.accept()
with conn:
    print("Connection from: ", addr)
    conn.sendall(cert_file_contents)
    print("Sent cert file")


############ GET ENCRYPTED SYM KEY AND ENCRYPTED FILE FROM CLIENT############
# Listen
server_socket.listen(5)
# Accept
conn, addr = server_socket.accept()
with conn:
    print("Connection from: ", addr)
    encrypted_sym = conn.recv(1024)

# Listen
server_socket.listen(5)
# Accept
conn, addr = server_socket.accept()
with conn:
    print("Connection from: ", addr)
    encrypted_file = conn.recv(1024)


print("Received encrypted sym and encrypted file")

# Write encrypted sym key to file
with open(os.getcwd() + "/serverfiles/encrypted_sym.txt", "wb") as f:
    f.write(encrypted_sym)

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
