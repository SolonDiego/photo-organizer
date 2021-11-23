import os
import shutil
from datetime import datetime
from PIL import Image

def folder_path_from_date(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m')

def photo_shooting_date(file):
    photo = Image.open(file)
    info = photo._getexif()
    if info:
        if 36867 in info:
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        else:
            date = datetime.fromtimestamp(os.path.getatime(file))
    if info is None:
        date = datetime.fromtimestamp(os.path.getatime(file))
    return date

def move_photo(file):
    new_folder = folder_path_from_date(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    shutil.move(file, new_folder + '/' + file)

print(photo_shooting_date('vovo.jpg'))

print(folder_path_from_date('vovo.jpg'))

print(move_photo('vovo.jpg'))

