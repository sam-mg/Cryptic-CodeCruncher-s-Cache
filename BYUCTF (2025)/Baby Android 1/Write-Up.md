# Baby Android 1

## Description
```
If you've never reverse engineered an Android application, now is the time!! Get to it, already!! Learn how they work!!
```

Upon analyzing the application in Jadx, we notice in `MainActivity` that there is a `Utilities` class containing a `cleanup()` method, which is invoked in the `onCreate()` method.

```java
package byuctf.downwiththefrench;

import android.app.Activity;
import android.widget.TextView;

/* loaded from: classes3.dex */
public class Utilities {
    private Activity activity;

    public Utilities(Activity activity) {
        this.activity = activity;
    }

    public void cleanUp() {
        TextView flag = (TextView) this.activity.findViewById(R.id.flagPart1);
        flag.setText("");
        TextView flag2 = (TextView) this.activity.findViewById(R.id.flagPart2);
        flag2.setText("");
        TextView flag3 = (TextView) this.activity.findViewById(R.id.flagPart3);
        flag3.setText("");
        .
        .
        .
        TextView flag28 = (TextView) this.activity.findViewById(R.id.flagPart28);
        flag28.setText("");
    }
}
```

This method clears the text of the TextViews. Additionally, the text is set to something else in the `MainActivity` method:
```java
TextView homeText = (TextView) findViewById(R.id.homeText);
homeText.setText("Too slow!!");
```

Examining the [layout file](./Files/activity_main.xml) for `MainActivity`, we find 29 TextViews with the IDs `homeText`, `flagPart1`, `flagPart2`, ..., `flagPart28`.

The simplest way to solve this challenge is to render the XML file. There are several ways to do this, but the easiest is in Android Studio. Simply use any existing Android project, copy the XML file to the `res/layout` folder, and render it.  
<p align="center">
  <img src="./Assests/XML%20Rendered.jpeg" alt="XML Rendered"/>
</p>

```
byuctf{android_piece_0f_c4ke}
```