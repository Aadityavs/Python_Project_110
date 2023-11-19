import os
import shutil

from_dir='C:/Users/user/Downloads'
to_dir='C:/Users/user/Documents/Document_files'

list_of_files=os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,extension=os.path.splitext(files)
    print(name)
    print(extension)