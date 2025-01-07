# kuli-ah forensik

## Description:
```
I just created secret message in image file but i want to make it secure so i transform it to audio file. But i think it's not secure enough so i archive it with password. I encrypt it with very strong password. I'am sure no one can crack it because my password is random 15 digit number in base 3. It's very very secure right? ... right??. Then i wrap my file within an image so no one can realize.

flag = TCF2024{<my secret message>}
```

## Write-Up:
First, let's use binwalk to extract the contents of this image file with the following command:
```bash
binwalk -e kobokanaeruluvluv.jpg
```

Upon extracting, we find a password-protected ZIP file. According to the description, the password is a 15-digit number in base 3. We can create a Python program to generate a wordlist for our brute-force attack:
```py
passwords = []
for i in range(3**15):
    password = ""
    num = i
    for _ in range(15):
        password = str(num % 3) + password
        num //= base
    passwords.append(password.zfill(15))

with open("numbers.txt", "w") as file:
    for password in passwords:
        file.write(password + "\n")
```

Next, we use John the Ripper to find the password for the zip file with the following commands:
```bash
zip2john E6C63.zip > zip.hash
john zip.hash --wordlist=Documents/numbers.txt # costum wordlist of numbers created by the python script
john --show zip.hash
```
Using this approach, we discover that the password is `012012010121022`. Extracting the zip file, we find a `.wav` file. Upon inspecting the spectrogram, nothing is immediately apparent.

So, we use the SSTV tool, which is available on [github](https://github.com/colaclanth/sstv).
```bash
sstv -d Robot36.wav -o out.png
```

This reveals the hidden image. With this message, we can construct the flag: `TCF2024{w0w_congrats_you_win}`.