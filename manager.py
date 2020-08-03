from moniter_sync import monitor_dir
from actions import handle_results

def main():
    monitor_dir(handle_results)

if __name__ == "__main__":
    main()