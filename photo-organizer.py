import os
import shutil
from datetime import datetime
from PIL import Image


class PhotoOrganizer:

    extensions = ['jpg', 'jpeg', 'png' 'JPG', 'JPEG', 'PNG']


    def folder_path_from_date(self, file):
        date = self.photo_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m')


    def photo_shooting_date(self, file):
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


    def move_photo(self, file):
        new_folder = self.folder_path_from_date(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)


    def organize(self):
        photos = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for filename in photos:            
            self.move_photo(filename) 
            

PO = PhotoOrganizer()
PO.organize()