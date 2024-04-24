import os
import sys
import configparser
from typing import Tuple
from wfc import paths, logger

SECTION_NAME = "Settings"
ENCODING = "utf-8"


def _get_config_values() -> Tuple[list[str], str, int, bool, int]:
    if not os.path.exists(paths.CONFIG_PATH):
        logger.log(
            logger.ERROR,
            f"{paths.CONFIG_FILE_NAME} not found! Should be at {paths.CONFIG_PATH}",
        )
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(paths.CONFIG_PATH, encoding=ENCODING)

    search_paths = (
        config[SECTION_NAME]["SEARCH_PATHS"]
        .replace(" ", "")
        .removesuffix(",")
        .split(",")
    )
    extractable_extensions = (
        config[SECTION_NAME]["EXTRACTABLE_EXTENSIONS"]
        .replace(" ", "")
        .removesuffix(",")
        .replace(",", "|")
    )
    days_until_deletion = int(config[SECTION_NAME]["DAYS_UNTIL_DELETION"])
    start_with_windows = config[SECTION_NAME]["START_WITH_WINDOWS"].lower() == "true"
    max_log_size_mb = int(config[SECTION_NAME]["MAX_LOG_SIZE_MB"])

    return (
        search_paths,
        extractable_extensions,
        days_until_deletion,
        start_with_windows,
        max_log_size_mb,
    )


data = _get_config_values()
