import re
from datetime import datetime
import logging
from typing import Tuple
from wfc import paths, popup


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
    size_saved = 0.0
    with open(paths.LOG_PATH, "r", encoding=ENCODING) as log_file:
        for line in log_file:
            if "Program startup" in line:
                continue

            timestamp, _, size, _ = _extract_line_data(line)
            if timestamp == "":
                continue
            timestamp_datetime = datetime.strptime(timestamp, DATE_FORMAT)

            if (current_date - timestamp_datetime).days <= 30:
                size_saved += float(size[:-3])

    size_saved /= 1024.0
    popup.show_notification(
        "There's nothing to delete!",
        f"You have saved {size_saved:.2f} GB in the last 30 days.",
    )


def _extract_line_data(line) -> Tuple[str, str, str, str]:
    # sourcery skip: extract-method, inline-variable, remove-unnecessary-else
    # Define regular expressions to match different parts of the log line
    timestamp_regex = r"(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})"
    filename_regex = r"FILE: (.*?) SIZE:"
    size_regex = r"SIZE: ([\d.]+) (.)B"
    reason_regex = r"REASON: (.+)"

    # Compile the regex patterns
    timestamp_match = re.search(timestamp_regex, line)
    filename_match = re.search(filename_regex, line)
    size_match = re.search(size_regex, line)
    reason_match = re.search(reason_regex, line)

    # Check if all parts were matched
    if timestamp_match and filename_match and size_match and reason_match:
        timestamp = timestamp_match[1]
        filename = filename_match[1]
        # Convert size to float (assuming MB for demonstration)
        size_value = float(size_match[1])
        if size_match[2] == "G":
            size_value *= 1024  # Convert to MB if size is in GB
        size = f"{size_value:.2f} MB"
        reason = reason_match[1]
        return timestamp, filename, size, reason
    else:
        # print(f"LINE FORMAT INVALID! {filename_match}")
        return "", "", "", ""


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
