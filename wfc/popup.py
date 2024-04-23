import os
import time
import win11toast


# from wfc import config


def tray_clicked():
    # os.startfile(config.data[0][0])  -> Downloads
    # os.startfile("::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")  -> This PC
    os.startfile("shell:RecycleBinFolder")


def show_notification(title: str, message: str) -> None:
    time.sleep(1)
    win11toast.toast(
        title,
        message,
        audio={"silent": "true"},
        duration="long",
        on_click=lambda args: tray_clicked(),
    )
