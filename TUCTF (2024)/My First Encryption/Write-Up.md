# My First Encryption

## Description
```
I just learned about xor! Apparently it's super strong, surely it can protect my secret file!
```

From the description, we can see that the `flag.jpeg` is encrypted using XOR with a key.  
We can determine the key by `XORing` the encrypted file's header with the header of the original file using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'cfe8cf'%7D,'Standard',false)To_Hex('None',0)&input=ZmZkOGZm).  
After this, we find the key as:
```hex
303030
```

Next, we can decrypt the `flag.jpeg` using the key `303030` with [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'303030'%7D,'Standard',false)Render_Image('Raw')).

We get the flag as:
```
TUCTF{kn0wn_pl@1nt3xt_15_dang3r0us}
```
![](./Assets/original_flag.jpg)