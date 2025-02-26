from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64

print(AESGCM(base64.b64decode("YWYwYjAyYjkzNmRhZjU3Yg==")).decrypt(base64.b64decode("TXdESVBYeWc1dldkbHNFaQ=="), base64.b64decode("XZdGZ7pi9Ih4wHL/8Mj0q8/o6i/utS2tIsigHXCaEzpTXgesqtnLNJMbagqYH67ut9dbxhXC28w="), None).decode())