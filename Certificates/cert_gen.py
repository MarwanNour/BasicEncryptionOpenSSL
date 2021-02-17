# Marwan Nour           marwan.nour@polytechnique.edu

import os
import sys

# input: identity, public key, CA's sk 

if (len(sys.argv) != 4):
    print("Incorrect syntax")
    print("python3 cert_gen.py <identity> <public_key> <CA_sk>")
    sys.exit(1)

identity = sys.argv[1]
pk_file = sys.argv[2]
ca_sk_file = sys.argv[3]

# print("arg[1] = " + identity)
# print("arg[2] = " + pk_file)
# print("arg[3] = " + ca_sk_file)

if (not os.path.isfile(os.getcwd() + "/" + pk_file)):
    print("Public key file doesn't exist")
    sys.exit(1)

if (not os.path.isfile(os.getcwd() + "/" + ca_sk_file)):
    print("CA's sk file doesn't exist")
    sys.exit(1)


####### Create certificate #######
# read pk file
pk = ''
with open(os.getcwd() + "/" + pk_file, "r") as f:
    pk = f.read()

print(pk)

# add identity to pk into a new file
file_name = identity + "_file_to_sign.txt"
with open(os.getcwd() + "/" + file_name, "w") as f:
    f.write(identity + "\n" + pk)

# Sign with CA sk
print("Signing...")
os.system("openssl dgst -sha256 -sign " + ca_sk_file +  " -out " + identity + "_signature.bin < " + file_name)
print("Done")