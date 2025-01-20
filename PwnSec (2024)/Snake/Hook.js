Java.perform(function () {
    var BigBoss = Java.use('com.pwnsec.snake.BigBoss');
    BigBoss.stringFromJNI.implementation = function (str) {
        var result = this.stringFromJNI(str);
        console.log(result);
        return result;
    };
    BigBoss.$new("Snaaaaaaaaaaaaaake");
});