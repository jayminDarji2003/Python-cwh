# shutil module in python
"""
    Function used to perform file based operations.
        1. copy(source, destination)
            - The copy function is used to copy the file.
        2. copytree(source, destination)
            - The copy function is used to copy the folder.
        3. move(source, destination)
            - The move function is used to move the file.
        4. rmtree(source, destination)
            - Remove the directory.
        5. make_archive(source,"zip", destination)
            - Make a zip folder.
        6. unpack_archive(source, destination)
            - unpack the zip file.
        
"""

import shutil
import os

# copy file
# shutil.copy("Day 85/python.png", "Day 87/python_copy.png")

# copy folder
# shutil.copytree("Day 86", "Day 87/copy_folder")

# move file
# shutil.move("Day 87/copy_folder", "rough")

# remove folder
# shutil.rmtree("Day 87/copy_folder")

# convert to zip file
# shutil.make_archive("my_new_zip", "zip","copy_folder")

# unpack the zip file
# shutil.unpack_archive("copy_folder", "my_new_zip.zip")
