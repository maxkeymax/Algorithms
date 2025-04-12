"""
Write a Python program to create multiple threads and print their names.
"""

import threading


def print_current_thread_name():
    current_thread = threading.current_thread()
    print(f"Current thread name: {current_thread.name}")


threads = []

for _ in range(10):
    thread = threading.Thread(target=print_current_thread_name)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
