# Baby Android 2

## Description
```
If you've never reverse engineered an Android application, now is the time!! Get to it, already!! Learn more about how they work!!
```

Upon loading the `MainActivity` class in Jadx, we notice a `FlagChecker` class containing a native method, `check()`, which accepts a string and returns a boolean. This method is invoked within the `onCreate` method of `MainActivity`:

```java
if (FlagChecker.check(flagAttempt)) {
    banner.setText("That's the right flag!!!");
} else {
    banner.setText("Nope! Try again if you'd like");
}
```

Next, let's examine the [native library](./Native%20Libraries/libbabyandroid.so) in [IDA](https://hex-rays.com/ida-free):

```c
int __cdecl Java_byuctf_babyandroid_FlagChecker_check(int a1, int a2, int a3){
    int StringUTFChars; // eax
    int i; // [esp+20h] [ebp-28h]
    unsigned __int8 v6; // [esp+2Fh] [ebp-19h]
    _BYTE v7[12]; // [esp+30h] [ebp-18h] BYREF
    unsigned int v8; // [esp+3Ch] [ebp-Ch]

    v8 = __readgsdword(0x14u);
    StringUTFChars = _JNIEnv::GetStringUTFChars(a1, a3, 0);
    std::string::basic_string<decltype(nullptr)>(v7, StringUTFChars);
    if ( sub_18C20(v7) == 23 ){
        for ( i = 0; i < 23; ++i ) {
            if ( *(char *)sub_18C50(v7, i) != aBycnuAacglyTtM[i * i % 47] ) {
                v6 = 0;
                goto LABEL_9;
            }
        }
        v6 = 1;
    } else {
        v6 = 0;
    }
    LABEL_9:std::string::~string(v7);
    return v6;
}
```

Here, `aBycnuAacglyTtM` is an array containing the string `bycnu)_aacGly~}tt+?=<_ML?f^i_vETkG+b{nDJrVp6=)=`.

We can reverse this using the [Python Script](Decrypt.py):

```
byuctf{c++_in_an_apk??}
```