# ezmobile

## Description
```
Just an ez mobile chall for n00bies.
```

No need to even install the file; we can just open the APK using [Jadx](https://github.com/skylot/jadx).

Since it is mentioned that this is an easy mobile challenge for beginners, we can assume that the flag is hardcoded in the source code. As usual, we can start by looking at the Strings file in the APK. We can see that there is a string called `flag` which contains the string:
```
UFdOU0VDe3czbHBfbjA3aCFuZ19TcDNDaTRsX0p1c3RfNF9GbDRnXyFuXzdoM19zN3Ihbmc1X3htbF9mIWwzfQ
```
This looks like a Base64 encoded string. We can decode it to get the flag:
```
PWNSEC{w3lp_n07h!ng_Sp3Ci4l_Just_4_Fl4g_!n_7h3_s7r!ng5_xml_f!l3}
```
