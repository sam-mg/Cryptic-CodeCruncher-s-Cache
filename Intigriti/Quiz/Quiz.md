# Quiz

## Description
```
Can you solve all the questions?
```

Let's see what's happening using jadx. We can see that the app retrieves 500 questions from the server and displays them one by one. We have to solve them within 60 seconds. If we solve all the questions, we will get the flag.

Technically, solving all the questions within 60 seconds is impossible. Therefore, we need an alternative approach. One idea is to intercept the request and replace the response for each question with `0 + 0`. This can be achieved using [HTTPToolkit](https://httptoolkit.com). However, this method results in a network error because of the delay in sending back the request. Thus, we need to explore another solution.

How about patching the app to always return true for the checks? We can do this using the following commands:
```bash
apktool d Quiz.apk
# Modify Smali Code
apktool b Quiz/
zipalign -v 4 Quiz/dist/quiz.apk Quiz/dist/quiz-aligned.apk
apksigner sign --ks Security\ Codes/Keystore/my-release-key.jks --out Quiz/dist/quiz-signed.apk Quiz/dist/quiz-aligned.apk
apksigner verify Quiz/dist/quiz-signed.apk
```

After this, we can install the app and solve the questions even with wrong answers. But now we face another issue: 500 questions. How about writing a Bash script to automate the clicks? We can use `adb` to automate the clicks. [Here is the script for it](Click%20Loop.sh).

After doing this, we can get the flag:
```
INTIGRITI{4_R34l_m0b1l3_h4ck3RRRRR}
```