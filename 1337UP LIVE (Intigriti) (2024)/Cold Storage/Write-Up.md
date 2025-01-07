# Cold Storage

## Description
```
People say you should store your keys offline in cold storage, so I built this offline app! I think that's what cold storage means 🤔
```

First, let's try installing the `.apk` [file](./Files/cryptovault.apk). However, when we attempt to install it, we encounter an issue: the app is not signed. To resolve this, we need to sign the app. You can refer to my previous writeup on how to sign an app [here](https://github.com/sam-mg/QuantumQuest-Qonnect/blob/main/HTB-Infiltrator/Challenges/Mobile/Anchored/Anchored.md).

After signing the [app](./Files/cryptovault-signed.apk), we can install and run it. Upon running, the app prompts for a key. To find this key, we need to reverse engineer the app.

We can use `apktool` to decompile the APK file and inspect its contents:
```zsh
apktool d cryptovault-signed.apk
```

After extracting the files, we find an `index.html` file containing a JavaScript function that checks for the pin:
```js
function unlockVault() {
    var pin = document.getElementById("pin").value.trim();
    if (pin === "7331") {
        document.getElementById("message").innerText = "Correct PIN!";
        retrieveencryptedKey();
    } else {
        document.getElementById("message").innerText = "Invalid PIN!";
    }
}
```

Entering the key `7331` reveals an encrypted key:
```
abf6c8abb5daabc8ab69d7846def17b19c6dae843a6dd7e1b1173ae16db184e0b86dd7c5843ae8dee15f
```

This hexadecimal string doesn't yield a proper output when decrypted using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=YWJmNmM4YWJiNWRhYWJjOGFiNjlkNzg0NmRlZjE3YjE5YzZkYWU4NDNhNmRkN2UxYjExNzNhZTE2ZGIxODRlMGI4NmRkN2M1ODQzYWU4ZGVlMTVm). We need to investigate further.

The `retrieveencryptedKey()` function is called when the pin is correct. Here's the obfuscated code:
```js
(function(_0x506dbf,_0x170411){const _0x12e004=a0_0x1707,_0x3fbe25=_0x506dbf();while(!![]){try{const _0x3b5636=parseInt(_0x12e004(0x122))/0x1*(parseInt(_0x12e004(0x117))/0x2)+-parseInt(_0x12e004(0x111))/0x3*(-parseInt(_0x12e004(0x121))/0x4)+-parseInt(_0x12e004(0x11b))/0x5*(parseInt(_0x12e004(0x11f))/0x6)+parseInt(_0x12e004(0x113))/0x7*(-parseInt(_0x12e004(0x11d))/0x8)+parseInt(_0x12e004(0x125))/0x9*(parseInt(_0x12e004(0x11e))/0xa)+-parseInt(_0x12e004(0x123))/0xb+parseInt(_0x12e004(0x120))/0xc*(parseInt(_0x12e004(0x112))/0xd);if(_0x3b5636===_0x170411)break;else _0x3fbe25['push'](_0x3fbe25['shift']());}catch(_0x18c02d){_0x3fbe25['push'](_0x3fbe25['shift']());}}}(a0_0x32dd,0x4ff3a));function a0_0x32dd(){const _0xb65be8=['9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5','length','map','38495LKnOYO','substr','8lZAZpw','6486450oYKfNK','402RerQLO','12MNesgS','4FulGyI','528939ZPevpd','861608xHrljL','split','9gQnkOh','toString','242571ENkSLa','502515FcoXSF','2628171KytvIJ','push','slice','join','2HiwuOL'];a0_0x32dd=function(){return _0xb65be8;};return a0_0x32dd();}function affineEncrypt(_0x1930bc,_0x36e79b,_0x33477e){return(_0x36e79b*_0x1930bc+_0x33477e)%0x100;}function xor(_0x3a38fa,_0x3c3309){return _0x3a38fa^_0x3c3309;}function a0_0x1707(_0x3d4d4c,_0x35b685){const _0x32dd9d=a0_0x32dd();return a0_0x1707=function(_0x170770,_0x4c15fe){_0x170770=_0x170770-0x110;let _0x3e6dad=_0x32dd9d[_0x170770];return _0x3e6dad;},a0_0x1707(_0x3d4d4c,_0x35b685);}function hexToBytes(_0x1d9eb0){const _0x3e7222=a0_0x1707;let _0x2ac99a=[];for(let _0x2363dc=0x0;_0x2363dc<_0x1d9eb0[_0x3e7222(0x119)];_0x2363dc+=0x2){_0x2ac99a[_0x3e7222(0x114)](parseInt(_0x1d9eb0[_0x3e7222(0x11c)](_0x2363dc,0x2),0x10));}return _0x2ac99a;}function reverseString(_0x22dcba){const _0x102ddd=a0_0x1707;return _0x22dcba[_0x102ddd(0x124)]('')['reverse']()[_0x102ddd(0x116)]('');}function keygen(){const _0x588caa=a0_0x1707;let _0x620410=_0x588caa(0x118),_0x19eb60=[_0x620410[_0x588caa(0x115)](0x0,0xe),_0x620410[_0x588caa(0x115)](0xe,0x1c),_0x620410[_0x588caa(0x115)](0x1c,0x2a),_0x620410[_0x588caa(0x115)](0x2a,0x38),_0x620410['slice'](0x38,0x46),_0x620410[_0x588caa(0x115)](0x46,0x54)],_0x4c2f5e=[_0x19eb60[0x3],_0x19eb60[0x5],_0x19eb60[0x1],_0x19eb60[0x4],_0x19eb60[0x2],_0x19eb60[0x0]],_0x22e526=reverseString(_0x4c2f5e['join']('')),_0x2051e9=hexToBytes(_0x22e526),_0x3788f1=0x9,_0x2afabe=0x7,_0x56285d=0x33,_0x351569=_0x2051e9['map'](_0x585a6f=>xor(affineEncrypt(_0x585a6f,_0x3788f1,_0x2afabe),_0x56285d));return _0x351569[_0x588caa(0x11a)](_0x5ca89b=>('0'+_0x5ca89b[_0x588caa(0x110)](0x10))[_0x588caa(0x115)](-0x2))[_0x588caa(0x116)]('');}
```

We can use [obf-io](https://obf-io.deobfuscate.io) to deobfuscate the code. After deobfuscation, we find the `keygen()` function, which generates the key. Here's the deobfuscated code:
```js
function affineEncrypt(_0x1930bc, _0x36e79b, _0x33477e) {
    return (_0x36e79b * _0x1930bc + _0x33477e) % 0x100;
}
function xor(_0x3a38fa, _0x3c3309) {
    return _0x3a38fa ^ _0x3c3309;
}
function hexToBytes(_0x1d9eb0) {
    let _0x2ac99a = [];
    for (let _0x2363dc = 0x0; _0x2363dc < _0x1d9eb0.length; _0x2363dc += 0x2) {
        _0x2ac99a.push(parseInt(_0x1d9eb0.substr(_0x2363dc, 0x2), 0x10));
    }
    return _0x2ac99a;
}
function reverseString(_0x22dcba) {
    return _0x22dcba.split('').reverse().join('');
}
function keygen() {
    let _0x19eb60 = ["9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5".slice(0x0, 0xe), 
                     "9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5".slice(0xe, 0x1c), "9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5".slice(0x1c, 0x2a), "9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5".slice(0x2a, 0x38), "9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5".slice(0x38, 0x46), "9425749445e494332757363353f5d6f50353b79445d7336343270373270366f586365753f546c60336f5".slice(0x46, 0x54)];
    let _0x4c2f5e = [_0x19eb60[0x3], _0x19eb60[0x5], _0x19eb60[0x1], _0x19eb60[0x4], _0x19eb60[0x2], _0x19eb60[0x0]];
    let _0x22e526 = _0x4c2f5e.join('').split('').reverse().join('');
    let _0x2051e9 = hexToBytes(_0x22e526);
    let _0x351569 = _0x2051e9.map(_0x585a6f => (0x9 * _0x585a6f + 0x7) % 0x100 ^ 0x33);
    return _0x351569.map(_0x5ca89b => ('0' + _0x5ca89b.toString(0x10)).slice(-0x2)).join('');
}
```

This reveals that the encryption uses an [Affine Cipher](https://en.wikipedia.org/wiki/Affine_cipher). We can now create a [Python script](Brute%20Force%20Script.py) to replicate this process, brute force the affine cipher, and retrieve the flag:
```
INTIGRITI{50_much_f0r_53cur3_c0ld_570r463}
```
