# Hijacker

## Description
```
I heard 4-digits pin is insecure, so I made a 6-digits pin system with custom keyboard to prevent keylogger for my android application.

You are required to create a malicious application to solve this challenge, that is by stealing the user's application PIN. Please submit your APK file to the [POC Tester](https://hijacker.chals.sekai.team/) once you have created a working solution.

❖ Note
The POC Tester will first run your malicious application and then the vulnerable application to simulate user interaction in real life. Any permission in your malicious application will be automatically granted. Submit the correct PIN to the connection below to get the flag.
```

Now, we have to create an application that uses an overlay to capture the coordinates from the [app](./Files/secure_app.apk). Here is the [Exploit App](./Exploit%20App/).

We can obtain the flag by submitting the correct PIN to the provided `ncat` server.

```
SEKAI{Ev3ry_K3yb0ard_1s_Ins3cur3}
```