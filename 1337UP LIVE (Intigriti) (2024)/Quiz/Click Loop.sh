#!/bin/bash
for i in {1..500}
do
    adb shell input tap 650 2200
done
echo "Tapped 500 times"