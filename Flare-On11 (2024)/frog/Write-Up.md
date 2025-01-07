# frog

We received a `.7z` file protected by the password `flare`. To unzip it, use the following command:
```bash
7z x frog.7z -pflare
```
Upon examining the `README.txt`, it appears that `pygame` is required. After installing it, we find some intriguing lines in the Python file:
```python
def GenerateFlagText(x, y):
    key = x + y*20
    encoded = "\xa5\xb7\xbe\xb1\xbd\xbf\xb7\x8d\xa6\xbd\x8d\xe3\xe3\x92\xb4\xbe\xb3\xa0\xb7\xff\xbd\xbc\xfc\xb1\xbd\xbf"
    return ''.join([chr(ord(c) ^ key) for c in encoded])
```
Running this script allows us to play the game, where we can use the arrow keys to move the frog.  

There are blocks that prevent us from reaching the statue. By commenting out a few lines in the Python code, we can remove these blocks and reach the statue, which then prints the flag.

```
welcome_to_11@flare-on.com
```