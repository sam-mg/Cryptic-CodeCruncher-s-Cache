# SealedRune

By running the `strings` command on the file, we extract the following Base64 string:
```
LmB9ZDNsNDN2M3JfYzFnNG1fM251cntCVEhgIHNpIGxsZXBzIHRlcmNlcyBlaFQ=
```

Decoding this with [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=TG1COVpETnNORE4yTTNKZll6Rm5ORzFmTTI1MWNudENWRWhnSUhOcElHeHNaWEJ6SUhSbGNtTmxjeUJsYUZRPQ) reveals:
```
.`}d3l43v3r_c1g4m_3nur{BTH` si lleps terces ehT
```

There’s clearly a string here, but it’s reversed. Let’s flip it using the same [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Reverse('Character')&input=TG1COVpETnNORE4yTTNKZll6Rm5ORzFmTTI1MWNudENWRWhnSUhOcElHeHNaWEJ6SUhSbGNtTmxjeUJsYUZRPQ) tool:
```
The secret spell is `HTB{run3_m4g1c_r3v34l3d}`.
```