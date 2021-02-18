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
b'marwan\n-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8GPkJzEEou4b9Q7F+d/N\nxjVXUROLTa9G04hNVc+3x1yJhExkNXKLf4jJBlr2txAX9YY3xorcW/5QoLrpbCpJ\nX2IX3lSO0AHOmFkuNA5lsvrkjYh+oaUTXWtfWdCv4iHP+rQYDQDPc4geFLf+5+ii\n/sgfbtXh97DMpOBOSp9/PePian9vHJlmdGRWKismvmTYSXvGIVkuZW7L0tr8F842\nMe3vHgiZFjhZZMy7v5QZxMUXeHDnoVW4SGc40MxEdD7v4Xtu5u6vTdz5r6O4GaQ0\nG+3iXXzKkxBdUanYOwsd+M1wpXTMpTwPPiq5LzXUtZPh6ZA8CHiRgVaHI6HfylS7\nOQIDAQAB\n-----END PUBLIC KEY-----\n'
b'\x01[\xc0s\xea\xb0\xecVTG\xa1\x80\xdf\x07\xa0\x9d\x84\xe3\xc1-\xf4\xec\xbbe\x12G\xe1\x9aG\x06\xb00p>C\x89\xbed\xd9u\xb3\xffc\tF \x14\x05\xe2\x08\x94\x06>[\xa7D\x06\xf4\x1e\xa2\xfb;\xd0\xda\x08\x85\x9c\x96d!wQ\xb0E\x8b\x85_g\xef\x85\x84\xb2\x83\xcbJx\xc2!\t,\xa9\xd2\xa7T\x07\xc8W`\x84\x18\xfa\xae0\xc2t\xb9\xf6(\xb9\x1b\xb3d\xafS+P{\x98\xf7\x0257\x15\x19w\xfe\rg8\xcb~8\xb2\xf4\xb1\xc3\xbf\n\\\xf0(v\xc6Xj\x90c\t\x13\x14\xabo\xf4\xdc\xcf\x92m\xbd\x01d\x99\xa4\xe8\x01/\xf3\x1d\xacmA\t\xc2\xf1\x9c\x9ab%\x84\xf5\xa9\xf8\x141D\xd4\x1b\xfe\x0b\xf7\xf6\x93\x1fS\xe9\xb29\xd0\x19\xf3\x10\xa3\x02\x1ai\x11\xb6\x13<|X\xe9\x8b{\x1a\xdd\xce\xe3\xa4\xf9\x8e\xb9\xa1\xb2\xb0\xa0\x8e\xb7\x15\xaf\x1c\xc6|jF\xde\x9d\xfbp2m\x1b\xbdB6\xf6\xd4\xdb`\x9f8\x1f\xde\x14\xf6\x08\xff'
Connection from:  ('127.0.0.1', 35800)
Sent original file
Connection from:  ('127.0.0.1', 35802)
Sent cert file
Connection from:  ('127.0.0.1', 35804)
Connection from:  ('127.0.0.1', 35806)
Received encrypted sym and encrypted file
DECRYPTING ...

BKIP1L0D
```
In another terminal:
```
└─$ python3 client.py CA_public.pem verif_out.txt
b'marwan\n-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8GPkJzEEou4b9Q7F+d/N\nxjVXUROLTa9G04hNVc+3x1yJhExkNXKLf4jJBlr2txAX9YY3xorcW/5QoLrpbCpJ\nX2IX3lSO0AHOmFkuNA5lsvrkjYh+oaUTXWtfWdCv4iHP+rQYDQDPc4geFLf+5+ii\n/sgfbtXh97DMpOBOSp9/PePian9vHJlmdGRWKismvmTYSXvGIVkuZW7L0tr8F842\nMe3vHgiZFjhZZMy7v5QZxMUXeHDnoVW4SGc40MxEdD7v4Xtu5u6vTdz5r6O4GaQ0\nG+3iXXzKkxBdUanYOwsd+M1wpXTMpTwPPiq5LzXUtZPh6ZA8CHiRgVaHI6HfylS7\nOQIDAQAB\n-----END PUBLIC KEY-----\n'
b'\x01[\xc0s\xea\xb0\xecVTG\xa1\x80\xdf\x07\xa0\x9d\x84\xe3\xc1-\xf4\xec\xbbe\x12G\xe1\x9aG\x06\xb00p>C\x89\xbed\xd9u\xb3\xffc\tF \x14\x05\xe2\x08\x94\x06>[\xa7D\x06\xf4\x1e\xa2\xfb;\xd0\xda\x08\x85\x9c\x96d!wQ\xb0E\x8b\x85_g\xef\x85\x84\xb2\x83\xcbJx\xc2!\t,\xa9\xd2\xa7T\x07\xc8W`\x84\x18\xfa\xae0\xc2t\xb9\xf6(\xb9\x1b\xb3d\xafS+P{\x98\xf7\x0257\x15\x19w\xfe\rg8\xcb~8\xb2\xf4\xb1\xc3\xbf\n\\\xf0(v\xc6Xj\x90c\t\x13\x14\xabo\xf4\xdc\xcf\x92m\xbd\x01d\x99\xa4\xe8\x01/\xf3\x1d\xacmA\t\xc2\xf1\x9c\x9ab%\x84\xf5\xa9\xf8\x141D\xd4\x1b\xfe\x0b\xf7\xf6\x93\x1fS\xe9\xb29\xd0\x19\xf3\x10\xa3\x02\x1ai\x11\xb6\x13<|X\xe9\x8b{\x1a\xdd\xce\xe3\xa4\xf9\x8e\xb9\xa1\xb2\xb0\xa0\x8e\xb7\x15\xaf\x1c\xc6|jF\xde\x9d\xfbp2m\x1b\xbdB6\xf6\xd4\xdb`\x9f8\x1f\xde\x14\xf6\x08\xff'
Verified OK

Random Sym Key : BKIP1L0D
ENCRYPTING SYM KEY...

ENCRYPTING FILE ...
```

## Features
Required:
- [x] Basic Client/Server implementation
- [x] Certificates

Optional:
- [ ] SSH-like feature
- [ ] MITM feature
