# Marwan Nour           marwan.nour@polytechnique.edu

import os
import sys

def verify(original_file, ca_pk_file, cert_file, output_file):
    os.system("openssl dgst -sha256 -verify " + ca_pk_file +  " -signature " + cert_file + " < " + original_file + " > " + output_file)

# input: original file, CA's pk, certificate, 

if (len(sys.argv) != 5):
    print("Incorrect syntax")
    print("python3 cert_verify.py <original_file> <CA_pk> <cert_file> <output_file>")
    sys.exit(1)

original_file = sys.argv[1]
ca_pk_file = sys.argv[2]
cert_file = sys.argv[3]
output_file = sys.argv[4]

# print("arg[1] = " + original_file)
# print("arg[2] = " + ca_pk_file)
# print("arg[3] = " + cert_file)


if (not os.path.isfile(os.getcwd() + "/" + ca_pk_file)):
    print("CA's pk file doesn't exist")
    sys.exit(1)

if (not os.path.isfile(os.getcwd() + "/" + cert_file)):
    print("Certificate file doesn't exist")
    sys.exit(1)


# Verify
print("Verifying...")
verify(original_file, ca_pk_file, cert_file, output_file)
print("Done")