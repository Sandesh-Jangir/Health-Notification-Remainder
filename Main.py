from plyer import notification
from win32com.client import Dispatch
import time

if __name__ == "__main__":
    while True:
        time.sleep(3600)
        description = "Walking 5 minutes, after every hour and seeing warming colours, relaxes our body and mind, and its also good for our Productivity"
        notification.notify(
        title = "Break Time",
        message = description,
        app_icon = "E:\Development\Py-Dev\Projects\Health Remainder\icon.ico",
        timeout =10
        )
        speech = Dispatch("Sapi.spVoice")
        speech.Speak("Enough Work sir, now its time for a short walk")
