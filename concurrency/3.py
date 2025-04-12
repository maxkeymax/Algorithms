"""
3. Even and Odd Printer Threads
Write a Python program that creates two threads to find and print even and odd 
numbers from 30 to 50.
"""

import threading

def print_even_numbers():
    for i in range(30, 51):
        if i % 2 == 0:
            print(i, end=' ')
            
def print_odd_numbers():
    print()
    for i in range(30, 51):
        if i % 2 != 0:
            print(i, end=' ')
            
even_tread = threading.Thread(target=print_even_numbers)
odd_tread = threading.Thread(target=print_odd_numbers)
even_tread.start()
odd_tread.start()
even_tread.join()
odd_tread.join()
