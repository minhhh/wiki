# ANDROID CLI CHEATSHEET
### Read log

```
    adb logcat
    adb logcat -v time

    adb logcat *:V # Get all message in verbose mode
    adb logcat xxxxxxx:V *:S # Get all message starts with xxxxx

    # Log by pid
    adb logcat | grep `adb shell ps | grep com.example.package | cut -c10-15`
```

### List package

```
    adb shell pm list package
    adb shell pm path com.example.someapp
    adb pull /data/app/com.example.someapp-2.apk
```

### Run a particular intent

```
    # Start by activity name
    adb shell 'am start -n com.qooapp.qoohelper/.activity.WelcomeActivity'

    # Start by action
    adb shell 'am start -a com.qooapp.qoohelper/.activity.WelcomeActivity'

    # add environment variable
    adb shell 'am start -a $(MYPACKAGEID).RUN -e server http://$(MYIP):$(MYPORT) -e game $(game) -e nativeLog $(MYNATIVELOG)'
```

### Install / Uninstall

```
    adb install file.apk
    adb install -r file.apk # replace

    # Install to a specific device
    adb -s "deviceIDfromlist" install file.apk

    adb shell am start -a android.intent.action.DELETE -d package:<your app package>
```

### Extracting APK file
* [Use `apktool`](http://ibotpeaches.github.io/Apktool/)

```
    apktool d /path/to/apk
    open res/values/strings.xml
```

## References
* [View android manifset from APK](http://stackoverflow.com/questions/4191762/how-to-view-androidmanifest-xml-from-apk-file)
* [Get apk from Android device](http://stackoverflow.com/questions/4032960/how-do-i-get-an-apk-file-from-an-android-device)
* [Adb shell to uninstall package](http://stackoverflow.com/questions/12949609/adb-shell-command-to-make-android-package-uninstall-dialog-appear)
* [Debugging with logcat](http://wiki.cyanogenmod.org/w/Doc:_debugging_with_logcat)

