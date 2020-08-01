import sys
import msvcrt
import pywintypes
import win32file
import win32con
import win32api
import win32event
import operations
import zipfile

FOLDER_TO_MONITER = "D:\MAX_EINSTEIN\Downloads"

FILE_LIST_DIRECTORY = 0x0001
FILE_ACTION_ADDED = 0x00000001
FILE_ACTION_REMOVED = 0x00000002

ASYNC_TIMEOUT = 5000

BUF_SIZE = 65536


def get_dir_handle(dir_name):
    flags_and_attributes = win32con.FILE_FLAG_BACKUP_SEMANTICS | win32con.FILE_FLAG_OVERLAPPED
    
    dir_handle = win32file.CreateFile(
        dir_name,
        FILE_LIST_DIRECTORY,
        (win32con.FILE_SHARE_READ |
         win32con.FILE_SHARE_WRITE |
         win32con.FILE_SHARE_DELETE),
        None,
        win32con.OPEN_EXISTING,
        flags_and_attributes,
        None
    )
    return dir_handle


def read_dir_changes(dir_handle, size_or_buf, overlapped):
    return win32file.ReadDirectoryChangesW(
        dir_handle,
        size_or_buf,
        True,
        (win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
         win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
         win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
         win32con.FILE_NOTIFY_CHANGE_SIZE |
         win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
         win32con.FILE_NOTIFY_CHANGE_SECURITY),
        overlapped,
        None
    )


def handle_results(results):
    for item in results:
        print("{}, ".format(item), end='')

        if(isinstance(item, list) and len(item) > 1):
            _action, _file = item[:1]
        else:
            _action, _file = item

        if _action == FILE_ACTION_ADDED:
            print("ADDED ", _file)
            fullpath = "{}\{}".format(FOLDER_TO_MONITER, _file)
            if(zipfile.is_zipfile(fullpath)):
                operations.unzip_file(fullpath)
        if _action == FILE_ACTION_REMOVED:
            print("DELETED", _file)


def esc_pressed():
    return msvcrt.kbhit() and ord(msvcrt.getch()) == 27


def monitor_dir_async(dir_handle):
    idx = 0
    buffer = win32file.AllocateReadBuffer(BUF_SIZE)
    overlapped = pywintypes.OVERLAPPED()
    overlapped.hEvent = win32event.CreateEvent(None, False, 0, None)
    while True:
        idx += 1
        read_dir_changes(dir_handle, buffer, overlapped)
        rc = win32event.WaitForSingleObject(overlapped.hEvent, ASYNC_TIMEOUT)
        if rc == win32event.WAIT_OBJECT_0:
            bufer_size = win32file.GetOverlappedResult(dir_handle, overlapped, True)
            results = win32file.FILE_NOTIFY_INFORMATION(buffer, bufer_size)
            handle_results(results)
        elif rc == win32event.WAIT_TIMEOUT:
            #print("    timeout...")
            pass
        else:
            print("Received {:d}. Exiting".format(rc))
            break
        if esc_pressed():
            break
    win32api.CloseHandle(overlapped.hEvent)


def monitor_dir(dir_name):
    dir_handle = get_dir_handle(dir_name)
    monitor_dir_async(dir_handle)
    win32api.CloseHandle(dir_handle)


def main():
    monitor_dir(FOLDER_TO_MONITER)


if __name__ == "__main__":
    main()
