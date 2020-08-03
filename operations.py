import os, shutil, sys
import zipfile
from zipfile import ZipFile
from config import categories, destinations


def get_file_extension(path):
    parts = path.split('.')
    if len(parts) == 1:
        return None
    elif len(parts) == 2:
        return parts[1]
    elif parts[-1] in categories["Programs"]:
        return parts[-1]
    else:
        return ('.'.join(parts[-2:]))


def classify_file(file):
    extn = get_file_extension(file)
    if(extn is not None):
        for (category, extensions) in categories.items():
            if extn in extensions:
                return category
    return None
        

def move_file(file, source, dest):
    try:
        from_file = os.path.join(source, file)
        to_file = os.path.join(dest, file)
        if not to_file == from_file:
            if os.path.isfile(from_file):
                if not os.path.exists(dest):
                    os.makedirs(dest)
                os.rename(from_file, to_file)
                print('moved: ' + str(to_file))
    except Exception as e:
        raise e
    return 


def copy_file(file, source, dest):
    try:
        from_file = os.path.join(source, file)
        to_file = os.path.join(dest, file)
        if not to_file == from_file:
            if os.path.isfile(from_file):
                if not os.path.exists(dest):
                    os.makedirs(dest)
                shutil.copyfile(from_file, to_file)
                os.remove(from_file)
                print('moved: ' + str(to_file))
    except Exception as e:
        print(file, sys.exc_info()[0])
        raise e      
    return 


def move_file_to_category(file, source, category):
    dest = destinations.get(category, source)
    try:
        if(source.split(':')[0] == dest.split(':')[0]):
            move_file(file, source, dest)
        else:
            copy_file(file, source, dest)
    except Exception as e:
        raise e  


def unzip_file(file, parent):
    filepath = os.path.join(parent, file)
    try:
        with ZipFile(filepath, 'r') as archive:
            archive.extractall(filepath.split('.')[0])
        os.remove(filepath)
        print("Unzipped: {}".format(file))
    except zipfile.BadZipFile:
        print('Error: Zip file is corrupted, File: {}', filepath)
    except zipfile.LargeZipFile:
        print('Error: File size if too large, File: {}', filepath)
    except:
        print("Error: Unknown, File: {}", filepath)