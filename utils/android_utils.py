import subprocess


def get_udid():
    device = subprocess.check_output(
        "adb devices", encoding="utf-8"
    ).splitlines()[1]
    if device:
        return device.split()[0]
    else:
        raise Exception("No active devices")


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Pixel 3",
        "systemPort": 8301,
        "resetKeyboard": True,
        "takesScreenshot": True,
        "udid": get_udid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
