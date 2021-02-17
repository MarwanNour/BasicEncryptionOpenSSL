# Marwan Nour           marwan.nour@polytechnique.edu

import os
import sys

# input: original file, CA's pk, certificate, 

if (len(sys.argv) != 4):
    print("Incorrect syntax")
    print("python3 cert_verify.py <original_file> <CA_pk> <cert_file>")
    sys.exit(1)

orignal_file = sys.argv[1]
ca_pk_file = sys.argv[2]
cert_file = sys.argv[3]

# print("arg[1] = " + orignal_file)
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
os.system("openssl dgst -sha256 -verify " + ca_pk_file +  " -signature " + cert_file + " < " + orignal_file)
print("Done")