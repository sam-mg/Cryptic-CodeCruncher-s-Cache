Java.perform(function() {
    var MainActivity = Java.use('com.pwnsec.firestorm.MainActivity');
    MainActivity.Password.implementation = function() {
        var result = this.Password();
        console.log('Password result: ' + result);
        return result;
    };
});