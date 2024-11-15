import string

def mod_inv(a, m):
    t, new_t, r, new_r = 0, 1, m, a
    while new_r:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    if r > 1: raise ValueError(f"{a} has no inverse mod {m}")
    return t + m if t < 0 else t

hex_str = '9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5'
key = [(mod_inv(9, 0x100) * (byte - 7)) % 0x100 ^ 0x33 for byte in [int(''.join([hex_str[i:i+14] for i in range(0, len(hex_str), 14)][i] for i in [3, 5, 1, 4, 2, 0])[::-1][i:i+2], 16) for i in range(0, len(''.join([hex_str[i:i+14] for i in range(0, len(hex_str), 14)][i] for i in [3, 5, 1, 4, 2, 0])[::-1]), 2)]]

result = ""
for i in range(42):
    for c in string.printable:
        if (mod_inv(9, 0x100) * (ord(c) - 7) % 0x100 ^ 0x33) == key[i]:
            result += c
            break
print(f"Flag: {result}")