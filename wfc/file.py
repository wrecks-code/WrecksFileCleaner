import contextlib
import shutil
import datetime
import os
import re
from typing import List, Tuple

from wfc.logger import log, INFO, ERROR
from wfc import popup, config, registry, paths

# TODO: Testmode toggle
TESTMODE = True


def get_things_to_delete() -> (
    Tuple[List[Tuple[str, float, str]], List[Tuple[str, float, str]]]
):
    (
        search_paths,
        extractable_extensions,
        days_until_deletion,
        _,
        _,
    ) = config.data

    pattern = rf".*\.({extractable_extensions})"
    _file_results = []
    _folder_results = []

    for search_path in search_paths:
        if not os.path.exists(search_path):
            log(ERROR, f"Path {search_path} not found!")
            continue

        for item in os.listdir(search_path):
            item_path = os.path.join(search_path, item)

            if (
                os.path.isdir(item_path)
                and get_days_since_creation(item_path) > days_until_deletion
            ):
                _folder_results.append((item_path, get_size_bytes(item_path), "age"))
            if os.path.isfile(item_path):
                if re.match(pattern, item) and has_extracted_folder(item_path):
                    _file_results.append(
                        (
                            item_path,
                            get_size_bytes(item_path),
                            "unpacked",
                        )
                    )
                    continue
                if get_days_since_creation(item_path) > days_until_deletion:
                    _file_results.append((item_path, get_size_bytes(item_path), "age"))

    return _file_results, _folder_results


def bytes_to_string(bytes_size: float) -> str:
    if bytes_size >= 1024**3:
        return f"{bytes_size / 1024**3:.2f} GB"
    else:
        return f"{bytes_size / 1024**2:.2f} MB"


def get_size_bytes(path: str) -> float:
    return_size_bytes = 0
    if os.path.isfile(path):
        return_size_bytes = os.path.getsize(path)
    if os.path.isdir(path):
        return_size_bytes = sum(
            os.path.getsize(os.path.join(root, file))
            for root, _, files in os.walk(path)
            for file in files
        )
    return return_size_bytes


def get_days_since_creation(path: str) -> int:
    if os.path.isfile(path):
        creation_time = os.path.getctime(path)
    elif os.path.isdir(path):
        creation_time = os.path.getctime(os.path.join(path, ""))
    else:
        return 0  # Return 0 if the path is neither a file nor a folder

    creation_date = datetime.datetime.fromtimestamp(creation_time)
    current_date = datetime.datetime.now()
    return (current_date - creation_date).days


def has_extracted_folder(file_path: str) -> bool:
    folder_path = os.path.splitext(file_path)[0]
    return os.path.isdir(folder_path)


def delete_file_or_folder(_path: str, _isfile: bool):
    if TESTMODE:
        return
    with contextlib.suppress(FileNotFoundError):
        if _isfile:
            os.remove(_path)
            return
        shutil.rmtree(_path)


def handle_startup() -> None:
    (
        _,
        _,
        _,
        start_with_windows,
        max_log_size_mb,
    ) = config.data

    registry.remove_from_autostart()
    if start_with_windows:
        registry.add_to_autostart()

    max_log_size_bytes = max_log_size_mb * 1024 * 1024
    if (
        os.path.exists(paths.LOG_PATH)
        and os.path.getsize(paths.LOG_PATH) > max_log_size_bytes
    ):
        with open(paths.LOG_PATH, "w", encoding=config.ENCODING):
            pass


def process_things():
    handle_startup()

    things_to_delete = get_things_to_delete()
    files_to_delete, folders_to_delete = things_to_delete

    bytes_to_delete = 0
    amount_reason_age = 0
    amount_reason_unpacked = 0

    for items, is_file in ((folders_to_delete, False), (files_to_delete, True)):
        for path, size_bytes, reason in items:
            basename = os.path.basename(path)

            if is_file:
                type_label = "FILE"
                if reason == "age":
                    amount_reason_age += 1
                elif reason == "unpacked":
                    amount_reason_unpacked += 1
            else:
                type_label = "DIR"

            log(
                INFO,
                f"{type_label}: {basename} SIZE: {bytes_to_string(size_bytes)} REASON: {reason}",
            )

            bytes_to_delete += size_bytes
            delete_file_or_folder(path, is_file)

    popup.show_notification(
        f"Deleted {bytes_to_string(bytes_to_delete)} from your computer.",
        f"{len(files_to_delete)} files and {len(folders_to_delete)} folders.\n"
        + f"{amount_reason_unpacked} files already unpacked, {amount_reason_age} too old ({config.data[2]} days)",
    )
