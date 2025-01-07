# MatryoshkaQR

## Description

```
Wow! This is a big QR code! I wonder what it says...?
```

We start with a [QR Code](./Files/qrcode.png). Scanning this QR code reveals a [Hex Dump](./Files/qrcode.txt). 

Using the provided [Python script](Script.py), we convert the Hex Dump back into an image. This process uncovers another [QR Code](./Files/QRCode(Final).png). Scanning this second QR code finally reveals our flag:

```
flag{01c6e24c48f48856ee3adcca00f86e9b}
```