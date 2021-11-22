import os
from datetime import datetime
from types import NoneType
from PIL import Image

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

print(photo_shooting_date('vovo.jpg'))

