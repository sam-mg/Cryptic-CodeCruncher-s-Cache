# checksum

We received a `.7z` file protected by the password `flare`. To unzip it, use the following command:
```bash
7z x checksum.7z -pflare
```

When we execute this `.exe` file using `wine`, we can see it performs some mathematical sum operations. At the end, it asks for a checksum.

Upon examining all the strings, we found one that stood out:
```
.rdata:00000000004D0A10	00000058	C	cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA==
```

This string is XORed with the first `11` bytes of another string:
```
FlareOn2024bad verb '%0123456789_/dev/stdout/dev/stderrCloseHandleOpenProcessGetFileTypeshort .....
```
which is essentially `FlareOn2024`.

When we XOR these two strings using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'UTF8','string':'FlareOn2024'%7D,'Standard',false)&input=Y1FvRlJRRXJYMVlBVncxelZRZEZVU3hmQVFOUkJYVU5BeEJTZTE1UUNWUlZKMXBRRXdkL1dGQlVBbEVsQ0ZCRlVubGFCMVVMQnlSZEJFRmRmVnRXVkE9PQ), we get this hex:
```
7fd7dd1d0e959f74c133c13abb740b9faa61ab06bd0ecd177645e93b1e3825dd
```

Let's try using this as the checksum and see if it works. And it did! However, we didn't get the flag yet.

Upon further inspection of the code, we discovered that the flag is stored as an image in the Cache folder, named `REAL_FLAREON_FLAG.JPG`.

Since we are using `wine` to run the `.exe` file, we need to navigate to the following path to retrieve the image:
```
~/.wine/drive_c/users/$(whoami)/AppData/Local/
```

We found the image there. When we opened it, we saw the flag:
![](./Assets/REAL_FLAREON_FLAG.JPG)

```
Th3_M4tH_Do_b3_mAth1ng@flare-on.com
```