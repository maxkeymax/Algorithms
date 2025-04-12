"""
7. Concurrent HTTP Requests
Write a Python program that performs concurrent HTTP requests using threads.

"""

import threading
import requests


def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")


# List of URLs to make requests to
urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
]
# Create and start threads for each URL
threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    thread.start()
    threads.append(thread)
# Wait for all threads to finish
for thread in threads:
    thread.join()
