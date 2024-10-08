# Intro to APK

## Description:
```
In the world of Android app development, Alex created a new app where hacking enthusiasts could test their skills with challenges. The signup process was Alex's way of ensuring that only the most skilled users could join. He worked hard to keep the app secure from unauthorized access. During this time, Alex encountered SkilledHackerLEET, a mysterious hacker known for testing digital defenses. Their back-and-forth challenge fascinated the app's users and showcased Alex's dedication to protecting his creation. In the midst of their rivalry, a puzzling message appeared: "To succeed, you must understand the app's flow and bypass its validation." This message added even more intrigue, making the app a place where only the best hackers could prove themselves.
```

## Write-Up:
To begin, let's open the `apk` file in `jadx-gui` using the following command:
```bash
jadx-gui alex_app.apk
```

There are two methods to solve this challenge:
1. **Using Online AES Decryption** - [Devglan](https://www.devglan.com/online-tools/aes-encryption-decryption)

2. **Using Credentials**  
    When signing up, use the following credentials to obtain the flag:
    ```
    Username: 1337
    Password: password
    ```
    These credentials can be obtained in various ways; for example, checking the shared preferences.
    ![untitled](Files/flag_screenshot.png)
    Additionally, reviewing the logcat will reveal the password.

The flag is: `TCP1P{v3ry_34sy_1snt_f0r_w4rm4p_j0st_k0tl1n}`