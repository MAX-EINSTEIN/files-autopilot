import json
from zipfile import ZipFile
from os.path import splitext

def get_file_extension(path):
    parts = path.split('.')
    if len(parts) == 1:
        return None
    elif len(parts) == 2:
        return parts[1]
    else:
        return ('.'.join(parts[-2:]))


def classify_file(filepath, config_filepath):
    categories = json.loads(config_filepath)
    extn = get_file_extension(filepath)
    if(extn is not None):
        for (category, extensions) in categories.items():
            if extn in extensions:
                return category
    return None
        
def move_file(self, filepath, source, dest):
        from_file = os.path.join(source, filepath)
        to_file = os.path.join(dest, filepath)
        if not to_file == from_file:
            print('moved: ' + str(to_file))
            if os.path.isfile(from_file):
                if not os.path.exists(dest):
                    os.makedirs(dest)
                os.rename(from_file, to_file)
        return 

def unzip_file(filename):
    try:
        with ZipFile(filename, 'r') as archive:
            archive.extractall(filename.split('.')[0])
    except zipfile.BadZipFile:
        print('Error: Zip file is corrupted, File: {}', filename)
    except zipfile.LargeZipFile:
        print('Error: File size if too large, File: {}', filename)
    except:
        print("Error: Unknown, File: {}", filename)
