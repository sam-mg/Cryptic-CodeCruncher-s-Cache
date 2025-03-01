# AndroidApplaketion

## Description
```
just an Android reg challenge
```

When we analyze the application in Jadx, we notice a native library named `ohgreat`, which contains around 600 boolean functions. Using IDA to examine these functions, we discover several mathematical operations that are computed and verified.

An example:
```c
bool __fastcall Java_com_lake_ctf_MainActivity_EPFL6f54db16d9b7cfd8241a92cfd9508f13635f1d51d11e0b47511d0376b2b19724(
    __int64 a1,
    __int64 a2,
    __int64 a3)
{
  _BYTE *v3; // rax

  v3 = (_BYTE *)(*(__int64 (__fastcall **)(__int64, __int64, _QWORD))(*(_QWORD *)a1 + 1352LL))(a1, a3, 0LL);
  return (v3[14] ^ (unsigned __int8)(v3[47] ^ v3[41])) == 76;
}
```

We have around 80 such functions to check:
```java
if (EPFL794e0d349c60e2cd18b028407c6ed39ed46025b5329af537b55ac256261b1035(obj) && EPFL4fe281842f9db50bc8ebf199c4226ac945608982855fbdfa5278479d3c5c2fc6(obj) && EPFL5777860ad7055bc1d6813df16e8d7ffbffe8407e8a2d08d7cf80a989f0498f47(obj) ...) {
        textView.setText("flag is correct!");
    } else {
        textView.setText("flag is wrong...");
    }
```

If all conditions are met, the flag is correct.

To find a text that satisfies all 80 functions, we can write a [Python script](./Equations%20Solver.py) using `z3` to solve all the equations.

```
EPFL{R3g1st3r_R3g1st3r_1n_L1b4rt.s0_wh3r3_w1ll_my_JN1_C4ll_g0?}
```