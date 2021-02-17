# Certificates-OpenSSL
Marwan Nour |  marwan.nour@polytechnique.edu

Basic Encryption and Certificates with OpenSSL for the Network Security course at École polytechnique.

Requirement: Python 3.x, openssl

## Usage
### Basic Client/Server
In one terminal:
```
python3 Basic/server.py
```
In another terminal: 
```
python3 Basic/client.py
```
### Certificates
Generate public/private keys files like:
```
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```
To generate a certificate:
```
python3 Certificates/cert_gen.py <identity> <public_key> <Certificate_Authority_sk>
```
To verify a certificate:
```
python3 Certificates/cert_verify.py <original_file> <Certificate_Authority_pk> <cert_file>
```

## Features
Required:
- [x] Basic Client/Server implementation
- [ ] Certificates

Optional:
- [ ] SSH-like feature
- [ ] MITM feature
