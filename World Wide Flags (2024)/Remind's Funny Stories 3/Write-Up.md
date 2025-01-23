# Remind's Funny Stories 3

## Description
```
Can you drop 10 million hearts for Remind's Funny Stories to get flag?
```

When we examine the APK in Jadx, we discover that the app is built using Flutter, allowing us to use [Blutter](https://github.com/worawit/blutter) to view the obfuscated code.

In the `main.dart` file, we find the following data:
```
Data: CXHoq5mV1jMA+63Sa7+IwhmhZWUXDL69B+wSB01uEQc63QWB0ZIeOiZtheLJpD0s2sC3s2+9FiWyRA+c1Y+vYw==
Key: 0h_g0d_sup3r_k3y_is_here_gsirjcu
IV: 16_bytes_key_len
```

We can decrypt this using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)AES_Decrypt(%7B'option':'UTF8','string':'0h_g0d_sup3r_k3y_is_here_gsirjcu'%7D,%7B'option':'UTF8','string':'16_bytes_key_len'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=Q1hIb3E1bVYxak1BKzYzU2E3K0l3aG1oWldVWERMNjlCK3dTQjAxdUVRYzYzUVdCMFpJZU9pWnRoZUxKcEQwczJzQzNzMis5RmlXeVJBK2MxWSt2WXc9PQ)

```
wwf{R3m1nD_fuNNy_5tori3s_1s_s0_3a5Y_51796E6B6C6565}
```