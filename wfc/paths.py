import os
import sys


def _get_base_path() -> str:
    if getattr(sys, "frozen", False):
        module_dir = os.path.dirname(sys.executable)
    else:
        module_dir = os.path.dirname(os.path.abspath(__file__))
    return _strip_package_name_from_path(module_dir)


def _strip_package_name_from_path(path) -> str:
    suffix = "wfc"  # Removed the backslash for platform independence
    return path[: -len(suffix)] if path.endswith(suffix) else path


# NAMES
APP_NAME = "WrecksFileCleaner"

EXE_FILE_NAME = f"{APP_NAME}.exe"
CONFIG_FILE_NAME = "config.ini"
LOG_FILE_NAME = "wfc.log"
ICON_FILE_NAME = "clean.ico"

BASE_PATH = _get_base_path()
EXE_PATH = os.path.join(BASE_PATH, EXE_FILE_NAME)

CONFIG_PATH = os.path.join(BASE_PATH, CONFIG_FILE_NAME)
LOG_PATH = os.path.join(BASE_PATH, LOG_FILE_NAME)
ICON_PATH = os.path.join(BASE_PATH, ICON_FILE_NAME)
