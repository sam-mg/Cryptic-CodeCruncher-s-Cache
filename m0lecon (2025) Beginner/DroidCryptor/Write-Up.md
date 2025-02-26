# DroidCryptor

## Description
```
One of my friends told me about this application that promised to keep your data safe. When I tried to encrypt the data, I found out later that there is no way to view it! Can you retrieve my message?
```

We are given an [apk file](./Files/app-debug.apk) and an [encrypted.txt](./Files/encrypted.txt) file. Let's take a closer look.

We can see that the Launcher Activity is focused on `com.droid.cryptor.MainActivity`, but when we open it, we can't find any useful information.

However, when we examine the `com.droid.cryptor.EncryptFragment`, we notice that it transitions to `com.droid.cryptor.EncryptedFragment`. There, we find the usage of the `com.droid.cryptor.AesLaboratory` class, which employs `AESGCM` encryption. In the same activity, we see that the key is hardcoded in Base64 and the IV is randomly generated. Interestingly, the IV is also printed as `Token` along with the `CipherText`.

```
Key: YWYwYjAyYjkzNmRhZjU3Yg== # Base64 Encoded
IV: TXdESVBYeWc1dldkbHNFaQ== # Base64 Encoded Randomly Generated
CipherText: XZdGZ7pi9Ih4wHL/8Mj0q8/o6i/utS2tIsigHXCaEzpTXgesqtnLNJMbagqYH67ut9dbxhXC28w=
```

Now, we can use a [Python Script](./Decrypt.py) to decrypt the message.
```
ptm{th3nk_y0u_f0r_r3st0r1ng_mY_m3ss4g3!}
```