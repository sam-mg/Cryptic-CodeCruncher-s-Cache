# Secure Vault

## Description
```
Can you log in?
```

Upon examining the Android Manifest file, we discover that the app is built using Flutter. We can utilize [Blutter](https://github.com/worawit/blutter) to extract the code. Our next task is to find the password to log in. By inspecting the `main.dart` file, we can locate the password.

The password is the base64 encoded version of the flag:
```
aXJvbkNURnswaF9teV9nMGQhIV95MHVfYnIwazNfaW50MF90aDNfNHBwXzRmNmUyMmNiYX0=
```

Decoding this string reveals the flag:
```
ironCTF{0h_my_g0d!!_y0u_br0k3_int0_th3_4pp_4f6e22cba}
```