# Cracknosaurus

## Description:
```
Budi is a vocational school student and a famous hacker in his class and has the mindset that things that exist in the real world can actually also be created in the digital world. Therefore, Budi tried to make a digital dinosaur called Cracknosaurus in the hope that the digital dinosaur he made could rule the world like the ancient dinosaurs of ancient times.

Cracknosaurus may look like an ordinary file, but you wouldn't know what Budi is hiding in this really extraordinary cracknosaurus image.
```

Hint:
```
Cracknosaurus actually have a digital friend, namely rockyousaurus, which when combined can solve everything.
```

## Write-Up:
To proceed with decrypting the file, we will utilize the `rockyou` wordlist for password brute-forcing using tools such as `John The Ripper` and `Fcrackzip`.

Once the password `tcpip` is identified, we can access the image file.
Subsequently, apply `stegseek` to perform another password brute-force attack:
```bash
stegseek flag.jpeg rockyou.txt
```

Following successful extraction, the flag is revealed: `TCP1P{m4st3r1ng_cr4ck1ng_w1th_r0cky0u!!!}`