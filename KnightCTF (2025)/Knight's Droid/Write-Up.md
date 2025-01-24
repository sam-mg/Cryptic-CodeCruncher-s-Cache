# Knight's Droid

## Description
```
For ages, a cryptic mechanical guardian has slumbered beneath the Knight’s Citadel. Some say it holds powerful secrets once wielded by ancient code-wielding Knights. Many have tried to reactivate the droid and claim its hidden knowledge—yet none have returned victorious. Will you be the one to solve its riddles and awaken this legendary machine?
```

When we examine the `MainActivity` using Jadx, we don't see much, but we do find another activity, `SecretKeyVerifier`. Upon closer inspection, something seems suspicious.

```java
public class SecretKeyVerifier {
    public static boolean verifyFlag(Context context, String userInput) {
        String fullPackageName = context.getPackageName();
        if (fullPackageName.length() < 20) {
            return false;
        }
        String firstTen = fullPackageName.substring(0, 10);
        int shift = computeShiftFromKey(firstTen);
        String encodedUserInput = droidMagic(userInput, shift);
        return "GYPB{_ykjcnwp5_GJECDP_u0q_c0p_uKqN_Gj1cd7_zN01z_}".equals(encodedUserInput);
    }
}
```

This leads us to the `droidMagic` function, which implements a simple `Caesar Cipher` with a shift of `22`. By decoding the encoded string, we can retrieve the flag.

```
KCTF{_congrat5_KNIGHT_y0u_g0t_yOuR_Kn1gh7_dR01d_}
```