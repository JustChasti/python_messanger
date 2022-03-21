import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.backends import default_backend

import base64
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

##########################генератор + расшифровка########################
"""
new_key = RSA.generate(2048)

private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

fd = open("privateKey.pem", "wb")
fd.write(private_key)
fd.close()

fd = open("publicKey.pem", "wb")
fd.write(public_key)
fd.close()
"""
"""
message = b'the text'

key = RSA.import_key(open('public_key.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
print(ciphertext)
print("\n\n")

base64_bytes = base64.b64encode(ciphertext)
base64_string = base64_bytes.decode("utf-8")
  
print(base64_string)
fd = open("data.txt", "w")
fd.write(base64_string)
fd.close()
"""
################зашифровка расшифровка#######################

"""
message = b'the text'

key = RSA.import_key(open('public_key.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
print(ciphertext)
print("\n\n")

ciphertext = b'VWuqWHvpaMOQ6mPfLfRVlyQXSFbuowe+doVlTqXrdQlIphVkUnj7ZMVVRa1SgP6KLCL6EnQa5oFXxY6Nq7/DoI91jkBcyC7Qx+k94wT+klaBmruO0tFBEkN2VPTLbURtrZTU2Xx6xJ44rr/UNgpPUS8iICMuaREbl1av5snJj3iUsZuQIa20GbH28EUM4cb1Vy7ra6pQ5/pZL0dHOfBefoF1dt1/x9ODqnzlcrTWrEm5x1FQS99qMa9ja7FMCcIeLCRAgn7YUPCC/HhY3fuOXK9LV99H1D4FmEl/MT0S22W9ClLpvE0sZr5zsz1MWsO4zIixHR63I/J6aZSnlOs0lQ=='
key = RSA.import_key(open('private_key.pem').read())
cipher = PKCS1_OAEP.new(key)
plaintext = cipher.decrypt(ciphertext)
print (plaintext.decode("utf-8"))
"""


key = load_pem_public_key(open('publicKey.pem').read().encode(), backend=default_backend())
dat = key.encrypt('Hello World. This is a test using Python3'.encode('utf-8'), padding.PKCS1v15())
ciphertext = base64.b64encode(dat)
print(ciphertext)

sentinel = get_random_bytes(20)
key = RSA.import_key(open('privateKey.pem').read())
cipher = PKCS1_v1_5.new(key)
# ciphertext = 'kMwBo5W6s7845YQEtx2n9Q2VkwG82fHYbChHzCrZzOIUq2dXu/XA/b+jk9gYZC4AF+2/mWGxSeVcZjOY2jkcZmOpufX1Y310DPG1DfbprHPfk6ZbFXA9CBf/mYgFdmHHy2g12sSERGyfTv/KwJi3E9CcTBLugGaHk5gQYKU9b9scFtiiSZ8fCjAH0snGvM8w2y9BYsEZd/04k7IK+yLYBioHd/vKPKdfsrVyRyss4gHUs5TjfTPRYxThgyanWyYA2vf7QKLQC5750cwHwLIloOQJSMnwwrZ0U2QeDFj18vpg/Gndw6ESyyR6zpjKZl3zTRlSbyY1Es7Ry4GiVB0n1A=='
plain_text = cipher.decrypt(base64.b64decode(str(ciphertext)[1:].encode('utf-8')), sentinel)
#plaintext = cipher.decrypt(ciphertext, sentinel, expected_pt_len=20)
print(plain_text.decode("utf-8"))
"""
key = load_pem_private_key(open('privateKey.pem').read().encode(), backend=default_backend())
plaintext = base64.b64encode(key.decrypt(ciphertext), padding.PKCS1v15())
print(plaintext.decode("utf-8"))
"""
