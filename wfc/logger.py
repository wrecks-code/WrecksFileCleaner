import re
from datetime import datetime
import logging
from typing import Tuple
from wfc import notification, paths


ENCODING = "utf-8"
INFO = "info"
ERROR = "error"
DATE_FORMAT = "%d.%m.%Y %H:%M:%S"

LOG: logging.Logger
STARTUP = True


def log(log_type: str, text: str):
    if log_type == ERROR:
        LOG.error(text)
    elif log_type == INFO:
        LOG.info(text)


def show_summary():
    current_date = datetime.now()
    size_saved_mb = 0.0
    with open(paths.LOG_PATH, "r", encoding=ENCODING) as log_file:
        for line in log_file:
            if "Program startup" in line:
                continue

            timestamp, _, size, _ = _extract_line_data(line)
            if timestamp == "":
                continue
            timestamp_datetime = datetime.strptime(timestamp, DATE_FORMAT)

            if (current_date - timestamp_datetime).days <= 30:
                size_saved_mb += float(size[:-3])  # Remove the unit (MB) before adding

    size_saved_gb = size_saved_mb / 1024.0
    notification.show_notification(
        "There's nothing to delete!",
        f"You have saved {size_saved_gb:.2f} GB in the last 30 days.",
    )


def _extract_line_data(line: str) -> Tuple[str, str, str, str]:
    filename_regex = r"(FILE|DIR): (.*?) SIZE: ([\d.]+) (GB|MB) REASON: (.+)"
    if not (match := re.search(filename_regex, line)):
        return "", "", "", ""
    timestamp = re.search(r"(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})", line)[1]
    filetype = match[1]
    size_value = float(match[3])
    size_unit = match[4]
    if size_unit == "GB":
        size_value *= 1024  # Convert GB to MB
    size = f"{size_value:.2f} MB"
    reason = match[5]
    return timestamp, filetype, size, reason


if STARTUP:
    logging.basicConfig(
        filename=paths.LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt=DATE_FORMAT,
    )
    LOG = logging.getLogger(__name__)
    LOG.critical("Program startup")
    STARTUP = False
