import os, sys
from enum import Enum, unique
import operations as opr


ACTIONS = {
    1: "CREATED",
    3: "UPDATED",
    5: "RENAMED"
}


def perform_actions(file, source, category):
    try:
        if category is None:
            print("Folder/File (no extn.): {}".format(file))
        elif(category == "Archives"):
            opr.unzip_file(file, source)
        elif(category == "Temp"):
            print(".tmp or .crdownload: {}".format(file))
        else:
            opr.move_file_to_category(file, source, category)
    except Exception as e:
        raise e
    return


def handle_results(folder, changes):
    for action, file in changes:
        category = opr.classify_file(file)
        print("{}, {}, {}\n".format(file, ACTIONS.get(action, "UNKNOWN"), category))
        
        if action in ACTIONS.keys():
            try:
                perform_actions(file, folder, category)
            except Exception as e:
                print("Unexpected error occured!", sys.exc_info()[0], e)
    return