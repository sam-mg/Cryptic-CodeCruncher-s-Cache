# Crack Me

## Description
```
Developed for SekaiCTF 2022 but never got a chance to release it. Can you log in and claim the flag?
```

When we look into the `MainActivity.java` file, we can see that this application is made using `React Native`. We know that `React Native` uses `JavaScript` for the logic, so we can get the code from the `assets/index.android.bundle` file.

We can use [UnMinify2](https://www.unminify2.com/) to view the `JS`. We can see a lot of functions. When we tried giving some random values, we can see that the app needs only the Admin. So, let's search for the `Admin` in the `JS` file.

```javascript
"admin@sekai.team" !== t.state.email || !1 === e.validatePassword(t.state.password) ? console.log("Not an admin account.") : console.log("You are an admin...This could be useful.");
```

So now we get the Admin's email. Now let's look into the `validatePassword` function.

```javascript
e.validatePassword = function(e) {
    if (17 !== e.length) return !1;
    return "03afaa672ff078c63d5bdb0ea08be12b09ea53ea822cd2acef36da5b279b9524" === R.default.AES.encrypt(e, (R.default.enc.Utf8.parse(b.default.KEY)), { iv: (R.default.enc.Utf8.parse(b.default.IV)) }).ciphertext.toString(R.default.enc.Hex)
}
```

So, the password is `17` characters long, and the `AES` encrypted value of the password should be the respective value. Let's now search for `KEY` and `IV` in the `JS` file.

```javascript
var _ = {
    LOGIN: "LOGIN",
    EMAIL_PLACEHOLDER: "user@sekai.team",
    PASSWORD_PLACEHOLDER: "password",
    BEGIN: "CRACKME",
    SIGNUP: "SIGN UP",
    LOGOUT: "LOGOUT",
    KEY: "react_native_expo_version_47.0.0",
    IV: "__sekaictf2023__"
};
```

Now we have the `KEY` and `IV`. We can decrypt the password using [CyberChef](https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'UTF8','string':'react_native_expo_version_47.0.0'%7D,%7B'option':'UTF8','string':'__sekaictf2023__'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=MDNhZmFhNjcyZmYwNzhjNjNkNWJkYjBlYTA4YmUxMmIwOWVhNTNlYTgyMmNkMmFjZWYzNmRhNWIyNzliOTUyNA). And we get the password as `s3cr3t_SEKAI_P@ss`.

Now let's try to log in with the Admin's email and the password we got. This is what we get:

![](/SekaiCTF%20%282024%29/Crack%20Me/Assets/Phone%20Image.png)

When checking for this in the `JS` file, we can see this:

```javascript
(0, M.signInWithEmailAndPassword)(s, t.state.email, t.state.password).then(function(e) {
    t.setState({
        verifying: !1
    });
    var n = (0, A.ref)(o, "users/" + e.user.uid + '/flag');
    (0, A.onValue)(n, function() {
        t.setState({
            verifying: !1
        }), t.setState({
            errorTitle: "Hello Admin",
            errorMessage: "Keep digging, you're almost there!"
        }), t.AlertPro.open()
    })
})
```

After reviewing the entire [JS Code](/SekaiCTF%20%282024%29/Crack%20Me/Files/Un%20Minified%20JS.js), we see that Firebase returns the flag. Although the flag is retrieved, it is not displayed. Let's use [HTTPToolkit](https://httptoolkit.com) to view the flag.

And we get the flag:
```
SEKAI{15_React_N@71v3_R3v3rs3_H@RD???}
```