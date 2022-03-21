import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.backends import default_backend

import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

"""
key = load_pem_public_key(open('publicKey.pem').read().encode(), backend=default_backend())
dat = key.encrypt('Hello World. This is a test using Python3'.encode('utf-8'), padding.PKCS1v15())
ciphertext = base64.b64encode(dat)
print(ciphertext)
"""
ciphertext = 'L81OeY5OAs66LwNw46wCd3U5tJuvd4lJow1GuiWu00WdN7p+7LKaZ/PcCKVsmYNFu5SWvjwSCWbJogj3s+pnJfOm88PeFHzntx/rcJHNZkOLDWuCqoacnfK59QYYFPkObE3vlveDYlud1bqZIo4Kx7ZMFKu/m6fjFdUIEIIqY+k='
sentinel = get_random_bytes(20)
key = RSA.import_key(open('privateKey.pem').read())
cipher = PKCS1_v1_5.new(key)
plain_text = cipher.decrypt(base64.b64decode(str(ciphertext).encode('utf-8')), sentinel)
print(plain_text.decode("utf-8"))
