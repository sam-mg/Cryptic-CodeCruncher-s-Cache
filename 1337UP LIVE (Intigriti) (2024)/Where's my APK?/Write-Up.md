# Where's my APK?

## Description
```
Can you achieve a leet download speed?

Note 1: Flag is not in the usual format. 
Note 2: Only non password protected files can be opened with the app.
```

In this challenge, we receive `.aab` files, which are Android App Bundles. Our task is to extract the APK from these bundles. To do this, we can use [bundletool](https://github.com/google/bundletool).

After installing bundletool, we can execute the following commands to install the APK on our emulator:
```bash
bundletool build-apks --bundle=Files/app-release.aab --output=Files/app-release.apks
mv Files/app-release.apks Files/app-release.zip
unzip Files/app-release.zip -d Files/app-release
adb install Files/app-release/universal.apk
```

Once installed, we notice that the app can download files from the domain `cybersharing.net`. However, when attempting to download a file, nothing happens. To troubleshoot, we need to intercept the traffic and investigate the issue.

After some trial and error, and a bit of frustration, we refer back to the description and realize that the download speed might be the key. We can use [HTTPToolkit](https://httptoolkit.com/) to intercept the traffic and modify the download speed.

Upon examining the `main.dart` file, we find that the download speed is set to `13371337`.

By changing the download speed to `13371337`, we successfully retrieve the flag:
```
WCLHGQOWOEQBNZALWSWDPSLQSLELA
```