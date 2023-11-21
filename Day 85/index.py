# command line utility using python
# The command line utility is used to perform some task. Here we are creating a utility where download the image from the internet. 

# To run this code :
#   --> Give commnd line arguments 
#     first : image url
#     second : file name

# ex : python index.py https://cdn.analyticsvidhya.com/wp-content/uploads/2023/07/1_m0H6-tUbW6grMlezlb52yw.png python.png

import argparse
import requests

def download_file(url,local_filename):
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return local_filename

parser = argparse.ArgumentParser()

# add command line arguments
parser.add_argument("url", help="url of the file to download")
parser.add_argument("output", help="by which name do you want to same your file ")

# parse the arguments
args = parser.parse_args()

# use the arguments in your code
print(args.url)
print(args.output)
download_file(args.url, args.output)