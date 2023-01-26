from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify


message = b"I love Cryptography"

private_key = RSA.generate(1024)
public_key = private_key.publickey()


# print(type(private_key),type(public_key))

private_pem = private_key.export_key().decode()

public_pem = public_key.export_key().decode()


# print(type(private_pem), type(public_pem))

with open('private.pem', 'w') as pr:
	pr.write(private_pem)
with open('public.pem', 'w') as pu:
	pu.write(public_pem)
 
 
# print('private.pem:')
# with open('private.pem', 'r') as f:
# 	print(f.read())
 
# print('public.pem:')
# with open('public.pem', 'r') as f:
#         print(f.read())

 
pr_key = RSA.import_key(open('private.pem', 'r').read())
pu_key = RSA.import_key(open('public.pem', 'r').read())


# print(type(pr_key), type(pu_key))

cipher = PKCS1_OAEP.new(key=pu_key)
cipher_text = cipher.encrypt(message)

# print(cipher_text)

decrypt = PKCS1_OAEP.new(key=pr_key)
decrypted_message = decrypt.decrypt(cipher_text)
print(decrypted_message)
