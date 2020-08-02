import moniter, actions

FOLDER_TO_MONITER = "D:\MAX_EINSTEIN\Downloads"
LOG_FILE = "log.txt"


def main():
    moniter.monitor_dir(FOLDER_TO_MONITER, actions.handle_results)

if __name__ == "__main__":
    main()