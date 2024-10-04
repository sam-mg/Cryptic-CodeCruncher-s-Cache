# Cattle

## Challenge Description

```
I know it's an esoteric challenge for a Capture the Flag, but could you herd these cows for me?
```

Upon opening the provided file, you'll notice a repetitive pattern of `MoO Moo`. This appears to be some form of encryption, and the mention of cows hints at a specific type of cipher.

A quick search on `cow encryption` leads us to [this GitHub repository](https://github.com/SkwalExe/cow-encryptor). While cloning the repo and following the README instructions is one way to decrypt the message, there's a more straightforward approach.

You can use online tools like [Cachesleuth](https://www.cachesleuth.com/cow.html). Simply paste the encrypted data into the tool, and it will decrypt it for you.

After decryption, you'll find the flag:
```
flag{6cd6392eb609c6ae4c332ef6a321d9dd}
```