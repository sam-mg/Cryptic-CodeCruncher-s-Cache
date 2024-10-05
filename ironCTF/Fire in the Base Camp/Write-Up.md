# Fire in the Base Camp

## Description

```
I was playing with the dice when I heard about the fire in the base camp. Can you get there on time?
```

Upon examining the `AndroidManifest.xml` file, we discovered the use of Firebase. In the `MainActivity`, we found that the value must be set to `9999999` to proceed with Firebase operations. This can be achieved using a [Frida Script](hook.js).

By setting the value, we can capture the traffic using [HTTP Toolkit](https://httptoolkit.com). When done correctly, the phone sends the value `please/give/me/the/flag` to the server. The server responds with the following message:

```json
{
    "t": "d",
    "d": {
        "r": 1,
        "b": {
            "s": "ok",
            "d": {
                "f1": "ironCTF{",
                "f2": "y0u_pu",
                "f3": "7_0u7_t",
                "f4": "h3_f1",
                "f5": "r3_1n_t",
                "f6": "h3_b4s",
                "f7": "3_c4mp",
                "f8": "_1f84a5",
                "f9": "c66ff5}"
            }
        }
    }
}
```

From this, we can extract the flag:

```
ironCTF{y0u_pu7_0u7_th3_f1r3_1n_th3_b4s3_c4mp_1f84a5c66ff5}
```