import os
from enum import Enum, unique

class Actions(Enum):
    FILE_ACTION_ADDED = 0x00000001
    FILE_ACTION_REMOVED = 0x00000002
    FILE_ACTION_MODIFIED = 0x00000003
    FILE_ACTION_RENAMED_OLD_NAME = 0x00000004
    FILE_ACTION_RENAMED_NEW_NAME = 0x00000005
    FILE_ACTION_UNKNOWN = 0x00000006

    def __str__(self):
        return str(self.name)


def handle_results(folder, changes):
    for action, file in changes:
        full_filename = os.path.join(folder, file)
        print("{}, {}\n".format(file, Actions(action)))
    
        if(action == Actions.FILE_ACTION_ADDED):
            pass
        elif(action == Actions.FILE_ACTION_REMOVED):
            pass
        elif(action == Actions.FILE_ACTION_MODIFIED):
            pass
        elif(action == Actions.FILE_ACTION_RENAMED_NEW_NAME):
            pass
        elif(action == Actions.FILE_ACTION_RENAMED_OLD_NAME):
            pass
        else:
            pass
        return