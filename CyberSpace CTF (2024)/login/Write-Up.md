# login

## Description
```
Just login!
```

When we look into the Android Manifest file, we see that the app is made using Flutter. We can use [Blutter](https://github.com/worawit/blutter) to get the code.

Now we have to find the login credentials to log in. By viewing the `main.dart` file, we can find the login credentials.

```
Username: 4dm1n
Password: Sup3rS3cr3tf0rMyS3cuR3L0ginApp // Password: Base64Decode("U3VwM3JTM2NyM3RmMHJNeVMzY3VSM0wwZ2luQXBw")
```

After we find that, we can get the flag by entering the above credentials.
```
CSCTF{SuP3r_S3cuRe_l0g1n_1234}
```

But, we can also get this without even using the emulator. We can see this hex string in the `main.dart` file:
```hex
10263367342860162200063963412e0c01563c1962547d5e38585c72440d
```
When we XOR this hex string with the password using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Base64','string':'U3VwM3JTM2NyM3RmMHJNeVMzY3VSM0wwZ2luQXBw'%7D,'Input%20differential',false)&input=MTAyNjMzNjczNDI4NjAxNjIyMDAwNjM5NjM0MTJlMGMwMTU2M2MxOTYyNTQ3ZDVlMzg1ODVjNzI0NDBk&oeol=VT), we can get the same flag.