import base64

with open('Huntress/Base64by32/Files/base64by32.txt', 'r') as file:
    encoded_text = file.read()
decoded_text = encoded_text
for _ in range(32):
    decoded_text = base64.b64decode(decoded_text).decode('utf-8')
print(decoded_text)