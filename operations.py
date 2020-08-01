from zipfile import ZipFile


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
