import os
import time
import win11toast
from wfc import paths

LOG_BTN_TXT = "Open Log"
DISMISS_BTN_TXT = "Dismiss"


def _tray_clicked(button: dict):
    button_name_pressed = button["arguments"].split(":")[1].strip()
    if button_name_pressed == LOG_BTN_TXT:
        os.startfile(paths.LOG_PATH)
    elif button_name_pressed == DISMISS_BTN_TXT:
        ...
        # sys.exit(0)


def show_notification(title: str, message: str):
    time.sleep(1)

    icon = {"src": paths.ICON_PATH, "placement": "appLogoOverride"}
    buttons = [LOG_BTN_TXT, DISMISS_BTN_TXT]

    win11toast.toast(
        title,
        message,
        audio={"silent": "true"},
        duration="long",
        on_click=lambda args: _tray_clicked(args),
        buttons=buttons,
        icon=icon,
    )
