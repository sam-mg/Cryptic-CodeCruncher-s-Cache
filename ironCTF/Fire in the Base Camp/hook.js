Java.perform(function() {
    var MainActivity = Java.use("com.example.app3.MainActivity");
    MainActivity.onCreate.overload('android.os.Bundle').implementation = function(bundle) {
        this.onCreate(bundle);
        var Integer = Java.use("java.lang.Integer");
        this.count.value = Integer.$new(9999998);
    };
});