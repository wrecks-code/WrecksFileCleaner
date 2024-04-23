import logging
from wfc import paths

ENCODING = "utf-8"
INFO = "info"
ERROR = "error"

LOG: logging.Logger
STARTUP = True


def log(log_type: str, text: str):
    if log_type == ERROR:
        LOG.error(text)
    elif log_type == INFO:
        LOG.info(text)


if STARTUP:
    logging.basicConfig(
        filename=paths.LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
    )
    LOG = logging.getLogger(__name__)
    LOG.critical("Program startup")
    STARTUP = False
