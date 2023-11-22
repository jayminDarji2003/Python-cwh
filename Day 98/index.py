# Multiprocessing in python.
# Execute multiple processes simultaneously then multiprocessing used.

import multiprocessing
import requests

def download_file(url, name):
    print(f"Started downloading {name}")

    response = requests.get(url)
    open(f"Day 98/images/{name}.jpg", "wb").write(response.content)

    print(f"Finished downloading {name}")

urls = [
    "https://images.pexels.com/photos/18105/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600",
    
    "https://images.pexels.com/photos/812264/pexels-photo-812264.jpeg?auto=compress&cs=tinysrgb&w=600",

    "https://images.pexels.com/photos/7974/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600",

    "https://images.pexels.com/photos/459654/pexels-photo-459654.jpeg?auto=compress&cs=tinysrgb&w=600",

    "https://images.pexels.com/photos/40185/mac-freelancer-macintosh-macbook-40185.jpeg?auto=compress&cs=tinysrgb&w=600"
]

if __name__ == "__main__":
    pros = []

    for i, url in enumerate(urls, start=1):
        p = multiprocessing.Process(target=download_file, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
