import os
import shutil

from_dir = "/Users/aneessh/downloads"
to_dir = "/Users/aneessh/desktop/document_files"

list_of_files = os.listdir(from_dir)

print(list_of_files)


for file in list_of_files:
    root,extension = os.path.splitext(file)
    print(root)
    print(extension)