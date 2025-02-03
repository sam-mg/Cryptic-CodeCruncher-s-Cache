# Flower App

## Description
```
I swiftly drew some flowers!
```

This is an iOS application, so let's use Ghidra to decompile the binary and examine the source code. Since the challenge is on iOS, it is quite challenging, so let's start with the basics.

First, let's find all the strings in the binary. When we look at the strings, we can see the `AES encrypted text`, `Key`, and `IV`.

```
AES encrypted text: 8XvXFKhm8YFfQShtVXcNZh5F8q0zBJMTnfBSh33SEr8r4hMWb/E2VJq20QO2Byef
Key: qQwrmkzuhJv6fzCF2XsxuaB+ZBtMEH+Cd3fpTgJpEM8=
IV: FjmNRmlNzMZYK8TbIItuVA==
```

We can decode this using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)AES_Decrypt(%7B'option':'Base64','string':'qQwrmkzuhJv6fzCF2XsxuaB%2BZBtMEH%2BCd3fpTgJpEM8%3D'%7D,%7B'option':'Base64','string':'FjmNRmlNzMZYK8TbIItuVA%3D%3D'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=OFh2WEZLaG04WUZmUVNodFZYY05aaDVGOHEwekJKTVRuZkJTaDMzU0VyOHI0aE1XYi9FMlZKcTIwUU8yQnllZg)

```
flag{congrats_on_swiftly_decoding_this}
```
