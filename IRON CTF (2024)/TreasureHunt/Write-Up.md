# TreasureHunt

## Description

```
I like colors and solving puzzles. What is better than having an app that brings both of them together?
```

Since this is a basic warm-up challenge, we can inspect the strings file of the application. There, we find:

```xml
<string name="part2">0f_4ndro1d_r3v?</string>
```

This gives us the first half of the flag. To find the other half, we need to explore the application further. After a thorough examination, we discover the following in `activity_main.xml`:

```xml
android:text="3ver_h3ard_"
```

Combining both parts with the flag format, we get the final flag:

```
ironCTF{3ver_h3ard_0f_4ndro1d_r3v?}
```