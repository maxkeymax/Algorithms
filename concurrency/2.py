"""
2. Concurrent File Downloader
Write a Python program to download multiple files concurrently using threads.
"""

from urllib.request import urlretrieve
import threading


def download_file(url, filename):
    print(f'Downloading {filename} from {url}')
    urlretrieve(url, filename)
    print(f'Finished downloading {filename}')
    
files_to_download = [
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Earth_Eastern_Hemisphere.jpg/640px-Earth_Eastern_Hemisphere.jpg",
        "filename": "earth_hemisphere.jpg"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/640px-PNG_transparency_demonstration_1.png",
        "filename": "transparency_demo.png"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/640px-Instagram_logo_2016.svg.png",
        "filename": "instagram_logo.png"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Coffee_cup_icon.svg/640px-Coffee_cup_icon.svg.png",
        "filename": "coffee_cup.png"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png",
        "filename": "phone_image.png"
    }
]

threads = []

for file_info in files_to_download:
    thread = threading.Thread(target=download_file, args=(file_info['url'], file_info['filename']))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()