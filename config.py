FOLDER_TO_MONITER = "D:\MAX_EINSTEIN\Downloads"

CONFIG_CATEGORIES = "E:/ProjectsHighway/files-autopilot/configs/files_classification.json"

CONFIG_DESTINATIONS = "E:/ProjectsHighway/files-autopilot/configs/files_test.json"

LOG_FILE = "logs.txt"


categories = {
    "Temp": ["tmp", "crdownload" ],
    "Music" : ["mp3", "aac", "flac", "ogg", "wma", "m4a", "aiff", "wav", "amr"] ,
    "Videos": ["flv", "ogv", "avi", "mp4", "mpg", "mpeg", "3gp", "mkv", "ts", "webm", "vob", "wmv"] ,
    "Pictures": ["png", "jpeg", "gif", "jpg", "bmp", "svg", "webp", "psd", "tiff", "jfif"] ,
    "Archives": ["rar", "zip", "7z", "gz", "bz2", "tar", "dmg", "tgz", "xz", "iso", "cpio"] ,
    "Documents": ["txt", "pdf", "doc", "docx", "odf", "xls", "xlsv", "xlsx,ppt", "pptx", "ppsx", "odp", "odt", "ods", "md", "json", "csv"] ,
    "Programs": ["exe", "msi"] 
}

destinations = {
    "Documents": "C:\\Users\\MAX_EINSTEIN\\OneDrive\\Documents",
    "Pictures": "C:\\Users\\MAX_EINSTEIN\\OneDrive\\Pictures",
    "Music": "D:\\MAX_EINSTEIN\\Music",
    "Videos": "D:\\MAX_EINSTEIN\\Videos",
    "Programs": "D:\\MAX_EINSTEIN\\Software Setups",
    "Unclassified": "D:\\MAX_EINSTEIN\\Unclassified Files"
}