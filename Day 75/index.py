# Exercise : To rename the file name 1.jpg till end of the file. only rename .jpg files. Use OS module.

import os

files = os.listdir("images")
count = 1

for f in files:
    if(f.endswith(".jpg")):
        os.rename(f"images/{f}", f"images/{count}.jpg")
        count = count + 1

