import os
import time
import win11toast
from wfc import paths

LOG_BUTTON_TXT = "Open Log"
RECYCLE_BIN_BUTTON_TXT = "Open Recycle Bin"


def tray_clicked(button: dict):
    button_name_pressed = button["arguments"].split(":")[1].strip()
    if button_name_pressed == LOG_BUTTON_TXT:
        os.startfile(paths.LOG_PATH)
    elif button_name_pressed == RECYCLE_BIN_BUTTON_TXT:
        os.startfile("shell:RecycleBinFolder")


def show_notification(title: str, message: str):
    time.sleep(1)

    icon = {"src": paths.ICON_PATH, "placement": "appLogoOverride"}

    win11toast.toast(
        title,
        message,
        audio={"silent": "true"},
        duration="long",
        on_click=lambda args: tray_clicked(args),
        buttons=[LOG_BUTTON_TXT, RECYCLE_BIN_BUTTON_TXT],
        icon=icon,
    )
