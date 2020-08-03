import os
import sys
import time
import win32file
import win32con

ACTIONS = {
    1: "CREATED",
    2: "TEST 1",
    3: "UPDATED",
    4: "RENAMED",
    5: "TEST 2"
}


FILE_LIST_DIRECTORY = 0x0001

FOLDER_TO_WATCH = "D:\MAX_EINSTEIN\Downloads"
RECORD_FILE = "record.txt"


dir_handle = win32file.CreateFile(
    FOLDER_TO_WATCH,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
)


def monitor_dir(handle_results):
    while True:
        try:
            results = win32file.ReadDirectoryChangesW(
                dir_handle,
                1024,
                True,
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
                win32con.FILE_NOTIFY_CHANGE_SIZE |
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                win32con.FILE_NOTIFY_CHANGE_SECURITY,
                None,
                None
            )

            handle_results(FOLDER_TO_WATCH, results)

        except KeyboardInterrupt:
            print("Program Terminated.\n")
            sys.exit(0)
