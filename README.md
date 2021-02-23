# Certificates-OpenSSL
Marwan Nour |  marwan.nour@polytechnique.edu

Basic Encryption and Certificates with OpenSSL for the Network Security course at École polytechnique.

Requirement: Python 3.x, openssl

## Usage
### Basic Client/Server
In one terminal:
```
cd Basic
python3 server.py
```
In another terminal: 
```
cd Basic
python3 client.py
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
Client/Server with certificates:
In one terminal:
```
cd Certificates
python3 server.py serverfiles/marwan_file_to_sign.txt serverfiles/marwan_signature.bin
```
In another terminal:
```
cd Certificates
python3 client.py CA_public.pem verif_out.txt   
```


### Demo Certificates
```
$ openssl genrsa -out private.pem 2048                     
Generating RSA private key, 2048 bit long modulus (2 primes)
........................................................................................+++++
............................................................+++++
e is 65537 (0x010001)

$ openssl rsa -in private.pem -pubout -out public.pem
writing RSA key
                                                                               
                                                                            
$ python3 cert_gen.py marwan serverfiles/public.pem CA_private.pem 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8GPkJzEEou4b9Q7F+d/N
xjVXUROLTa9G04hNVc+3x1yJhExkNXKLf4jJBlr2txAX9YY3xorcW/5QoLrpbCpJ
X2IX3lSO0AHOmFkuNA5lsvrkjYh+oaUTXWtfWdCv4iHP+rQYDQDPc4geFLf+5+ii
/sgfbtXh97DMpOBOSp9/PePian9vHJlmdGRWKismvmTYSXvGIVkuZW7L0tr8F842
Me3vHgiZFjhZZMy7v5QZxMUXeHDnoVW4SGc40MxEdD7v4Xtu5u6vTdz5r6O4GaQ0
G+3iXXzKkxBdUanYOwsd+M1wpXTMpTwPPiq5LzXUtZPh6ZA8CHiRgVaHI6HfylS7
OQIDAQAB
-----END PUBLIC KEY-----

Signing...
Done                                                                           
                                
$ mv marwan_signature.bin serverfiles/
                                                                   
$ mv marwan_file_to_sign.txt serverfiles/
```
In one terminal:
```
└─$ python3 server.py serverfiles/marwan_file_to_sign.txt serverfiles/marwan_signature.bin
Connection from:  ('127.0.0.1', 50736)
Sent original file
b'marwan\n-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8GPkJzEEou4b9Q7F+d/N\nxjVXUROLTa9G04hNVc+3x1yJhExkNXKLf4jJBlr2txAX9YY3xorcW/5QoLrpbCpJ\nX2IX3lSO0AHOmFkuNA5lsvrkjYh+oaUTXWtfWdCv4iHP+rQYDQDPc4geFLf+5+ii\n/sgfbtXh97DMpOBOSp9/PePian9vHJlmdGRWKismvmTYSXvGIVkuZW7L0tr8F842\nMe3vHgiZFjhZZMy7v5QZxMUXeHDnoVW4SGc40MxEdD7v4Xtu5u6vTdz5r6O4GaQ0\nG+3iXXzKkxBdUanYOwsd+M1wpXTMpTwPPiq5LzXUtZPh6ZA8CHiRgVaHI6HfylS7\nOQIDAQAB\n-----END PUBLIC KEY-----\n'
b'ACK File'
Sent cert file
b'\x01[\xc0s\xea\xb0\xecVTG\xa1\x80\xdf\x07\xa0\x9d\x84\xe3\xc1-\xf4\xec\xbbe\x12G\xe1\x9aG\x06\xb00p>C\x89\xbed\xd9u\xb3\xffc\tF \x14\x05\xe2\x08\x94\x06>[\xa7D\x06\xf4\x1e\xa2\xfb;\xd0\xda\x08\x85\x9c\x96d!wQ\xb0E\x8b\x85_g\xef\x85\x84\xb2\x83\xcbJx\xc2!\t,\xa9\xd2\xa7T\x07\xc8W`\x84\x18\xfa\xae0\xc2t\xb9\xf6(\xb9\x1b\xb3d\xafS+P{\x98\xf7\x0257\x15\x19w\xfe\rg8\xcb~8\xb2\xf4\xb1\xc3\xbf\n\\\xf0(v\xc6Xj\x90c\t\x13\x14\xabo\xf4\xdc\xcf\x92m\xbd\x01d\x99\xa4\xe8\x01/\xf3\x1d\xacmA\t\xc2\xf1\x9c\x9ab%\x84\xf5\xa9\xf8\x141D\xd4\x1b\xfe\x0b\xf7\xf6\x93\x1fS\xe9\xb29\xd0\x19\xf3\x10\xa3\x02\x1ai\x11\xb6\x13<|X\xe9\x8b{\x1a\xdd\xce\xe3\xa4\xf9\x8e\xb9\xa1\xb2\xb0\xa0\x8e\xb7\x15\xaf\x1c\xc6|jF\xde\x9d\xfbp2m\x1b\xbdB6\xf6\xd4\xdb`\x9f8\x1f\xde\x14\xf6\x08\xff'
b'ACK Cert'
Received Encrypted Sym Key
b'\xde6\xa3KD\xd03\xe7\xfe\x0ew\xfdx\xb5k`\x07\x90\x87\xaf.\x11k{\x0f\xbc2C\xbe`Y\n\xaf\x14s\xb9\x88\xb3\xc4\x12\xb3\x01\x9f\r\x1c\x0e\x11\x8a\xd0\xf8X\xdd\xfa}\x17\xf8\xd8T\xd6\xba>\xa2\x01\x8f\x0bXCO\xc9R"+2\xa9S6t\xbf~C\xaf\xba\x83\x10|\x920P/\xe2\x9b\x06vL6\x93\xde\xdcT^kb\xb2\xe0\xa6g\xb9\xbcR@\x92\xd7\x87\x8c\x03?\xa3OE\xe5\xd7\xa6\xbfb\xc9\x97\xee\xbbt9\x93\x14}\x00y,\xfc\xafo\x9e\x96\xc1\n\xccQ:\x9d\njrg_[\x95\xa1\xcb\x97E\xed\xf9\x9c2`+>\x9b\x05\xe9\xa4\x12}b\x8b\x82^\xb9\x03\x92\xe4\x93\x1a\xd1\xd4;=\xdek\xc5\x18\xcd\x9e\xf2\x0f\t&\x92`S\xff\xbbunv\x82\xb1\xce\xe3PjR\x04\xa1)?\xd9\xd4\x19\xaa,\xc0\xe8\x16%U\xd1ON4F\x08\x0b\xb5\x0f\xa4\x8b-=W9p\xdc+\xbe\x9e\xcfC\x0by\xda,;\xa9W\xbf\xaa]'
Received Encrypted File
b'U2FsdGVkX19qdhfXae8vLOk5veeXYcilhALgGfURDhabzXRXzaLZGrFamC6GX9OM\n'
DECRYPTING ...

A5FPR0CO
```
In another terminal:
```
└─$ python3 client.py CA_public.pem verif_out.txtReceived file
b'marwan\n-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8GPkJzEEou4b9Q7F+d/N\nxjVXUROLTa9G04hNVc+3x1yJhExkNXKLf4jJBlr2txAX9YY3xorcW/5QoLrpbCpJ\nX2IX3lSO0AHOmFkuNA5lsvrkjYh+oaUTXWtfWdCv4iHP+rQYDQDPc4geFLf+5+ii\n/sgfbtXh97DMpOBOSp9/PePian9vHJlmdGRWKismvmTYSXvGIVkuZW7L0tr8F842\nMe3vHgiZFjhZZMy7v5QZxMUXeHDnoVW4SGc40MxEdD7v4Xtu5u6vTdz5r6O4GaQ0\nG+3iXXzKkxBdUanYOwsd+M1wpXTMpTwPPiq5LzXUtZPh6ZA8CHiRgVaHI6HfylS7\nOQIDAQAB\n-----END PUBLIC KEY-----\n'
Received cert
b'\x01[\xc0s\xea\xb0\xecVTG\xa1\x80\xdf\x07\xa0\x9d\x84\xe3\xc1-\xf4\xec\xbbe\x12G\xe1\x9aG\x06\xb00p>C\x89\xbed\xd9u\xb3\xffc\tF \x14\x05\xe2\x08\x94\x06>[\xa7D\x06\xf4\x1e\xa2\xfb;\xd0\xda\x08\x85\x9c\x96d!wQ\xb0E\x8b\x85_g\xef\x85\x84\xb2\x83\xcbJx\xc2!\t,\xa9\xd2\xa7T\x07\xc8W`\x84\x18\xfa\xae0\xc2t\xb9\xf6(\xb9\x1b\xb3d\xafS+P{\x98\xf7\x0257\x15\x19w\xfe\rg8\xcb~8\xb2\xf4\xb1\xc3\xbf\n\\\xf0(v\xc6Xj\x90c\t\x13\x14\xabo\xf4\xdc\xcf\x92m\xbd\x01d\x99\xa4\xe8\x01/\xf3\x1d\xacmA\t\xc2\xf1\x9c\x9ab%\x84\xf5\xa9\xf8\x141D\xd4\x1b\xfe\x0b\xf7\xf6\x93\x1fS\xe9\xb29\xd0\x19\xf3\x10\xa3\x02\x1ai\x11\xb6\x13<|X\xe9\x8b{\x1a\xdd\xce\xe3\xa4\xf9\x8e\xb9\xa1\xb2\xb0\xa0\x8e\xb7\x15\xaf\x1c\xc6|jF\xde\x9d\xfbp2m\x1b\xbdB6\xf6\xd4\xdb`\x9f8\x1f\xde\x14\xf6\x08\xff'
Verified OK

Random Sym Key : A5FPR0CO
ENCRYPTING SYM KEY...

Sent encrypted sym file
b'\xde6\xa3KD\xd03\xe7\xfe\x0ew\xfdx\xb5k`\x07\x90\x87\xaf.\x11k{\x0f\xbc2C\xbe`Y\n\xaf\x14s\xb9\x88\xb3\xc4\x12\xb3\x01\x9f\r\x1c\x0e\x11\x8a\xd0\xf8X\xdd\xfa}\x17\xf8\xd8T\xd6\xba>\xa2\x01\x8f\x0bXCO\xc9R"+2\xa9S6t\xbf~C\xaf\xba\x83\x10|\x920P/\xe2\x9b\x06vL6\x93\xde\xdcT^kb\xb2\xe0\xa6g\xb9\xbcR@\x92\xd7\x87\x8c\x03?\xa3OE\xe5\xd7\xa6\xbfb\xc9\x97\xee\xbbt9\x93\x14}\x00y,\xfc\xafo\x9e\x96\xc1\n\xccQ:\x9d\njrg_[\x95\xa1\xcb\x97E\xed\xf9\x9c2`+>\x9b\x05\xe9\xa4\x12}b\x8b\x82^\xb9\x03\x92\xe4\x93\x1a\xd1\xd4;=\xdek\xc5\x18\xcd\x9e\xf2\x0f\t&\x92`S\xff\xbbunv\x82\xb1\xce\xe3PjR\x04\xa1)?\xd9\xd4\x19\xaa,\xc0\xe8\x16%U\xd1ON4F\x08\x0b\xb5\x0f\xa4\x8b-=W9p\xdc+\xbe\x9e\xcfC\x0by\xda,;\xa9W\xbf\xaa]'
b'ACK Sym key'
ENCRYPTING FILE ...

Sent encrypted file
b'U2FsdGVkX19qdhfXae8vLOk5veeXYcilhALgGfURDhabzXRXzaLZGrFamC6GX9OM\n'
b'ACK Enc file'
```

## Features
Required:
- [x] Basic Client/Server implementation
- [x] Certificates

Optional:
- [ ] SSH-like feature
- [ ] MITM feature
