# Snake

## Note
```
Make sure to run the mobile application on Android API 28 or less (Android 9 or less).
```

When we open the application in Jadx, we can see that the app is checking for Root detection. We can bypass these checks by returning `false` to the functions that check for Root detection.

After making these changes, we need to patch the application, using [HTB - Anchored](https://github.com/sam-mg/QuantumQuest-Qonnect/blob/main/HTB-Infiltrator/Challenges/Mobile/Anchored/Anchored.md) as a reference.

Next, we use `adb` to trigger the `MainActivity` with specific extras such as:
```java
String stringExtra = intent.getStringExtra("SNAKE");
intent.hasExtra("SNAKE") && stringExtra.equals("BigBoss")
```

We can use the following command to trigger the `MainActivity` with the specific extras:
```bash
adb shell am start -n com.pwnsec.snake/.MainActivity -e SNAKE BigBoss
```

We can see a class `BigBoss`. Let's try calling it using [Frida Script](./Hook.js). However, it doesn't work as there is Frida detection in the application.

Now, we can access it using the `Skull_Face.yml` in the `External Storage`. We have to exploit the YAML vulnerability. We can use the following payload in the `Skull_Face.yml` file:
```yaml
!!com.pwnsec.snake.BigBoss ["Snaaaaaaaaaaaaaake"]
```

Using this, we can get the flag in the `Logcat`:
```
PWNSEC{W3'r3_N0t_T00l5_0f_The_g0v3rnm3n7_0R_4ny0n3_3ls3}
```