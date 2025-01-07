# No need for Brutus

## Description

```
A simple message for you to decipher.
```
Encrypted Text [Here](./Files/No%20need%20for%20Brutus.txt)

```
Submit the original plaintext hashed with MD5, wrapped between the usual flag format: flag{}

Ex: If the deciphered text is "hello world", the MD5 hash would be 5eb63bbbe01eeed093cb22bb8f5acdc3, and the flag would be flag{5eb63bbbe01eeed093cb22bb8f5acdc3}.
```

To identify the type of encryption, we can use some [Online Cipher Identifying Tools](https://www.boxentriq.com/code-breaking/cipher-identifier). Given the clue that it might be a Caesar Cipher, we can brute force it using [dCode](https://www.dcode.fr/caesar-cipher).

After analysis, we find that the key is `16`. Thus, the decrypted text is:
```
caesarissimplenoneedforbrutus
```

Next, we hash it using an online MD5 tool.

Finally, we submit the flag:
```
flag{c945bb2173e7da5a292527bbbc825d3f}
```