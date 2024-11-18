# Firestorm

## Description
```
Descriptions are boring, just solve the challange meh!
```

When we open the app in JADX, we find a function called `password` that is not called anywhere in the code. This function takes a string from the string file, slices and concatenates it to form another string. This string is then sent to the native library `libfirestorm.so`, which performs some operations on it and returns a string.

```java
static {
    System.loadLibrary("firestorm");
}

public native String generateRandomString(String str);

public String Password() {
    StringBuilder sb = new StringBuilder();
    String string = getString(R.string.Friday_Night);
    String string2 = getString(R.string.Author);
    String string3 = getString(R.string.JustRandomString);
    String string4 = getString(R.string.URL);
    String string5 = getString(R.string.IDKMaybethepasswordpassowrd);
    String string6 = getString(R.string.Token);
    sb.append(string.substring(5, 9));
    sb.append(string4.substring(1, 6));
    sb.append(string2.substring(2, 6));
    sb.append(string5.substring(5, 8));
    sb.append(string3);
    sb.append(string6.substring(18, 26));
    return generateRandomString(String.valueOf(sb));
}
```

We can get the final string using Frida by calling that function. [Here](Getting%20Result%20-%20Hook.js) is the script to get the password.

After doing that, we see that it is some kind of password. In the strings they used and the strings present in the `strings.xml` file, we notice they are using some kind of connection with Firebase. So, we try to log in with the password we got from the above script and use Python to get the flag using the [script](Firebase%20Connection.py). We successfully log in and retrieve the flag.

```
PWNSEC{C0ngr4ts_Th4t_w45_4N_345y_P4$$w0rd_t0_G3t!!!_0R_!5_!t???}
```