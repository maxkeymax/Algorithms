"""
4. Multithreaded Factorial Calculator
Write a Python program to calculate the factorial of a number using multiple threads.
"""

import threading


def factorial(n):
    if n == 0 or n == 1:  # Base case: 0! = 1 and 1! = 1
        return 1
    else:
        return n * factorial(n - 1)


# Example usage: Calculate the factorial of 5 using multiple threads


def get_thread_info(n: int):
    result = factorial(n)
    print(f"Thread {threading.get_native_id()} is calculating {result}!")


number = 5

thread1 = threading.Thread(target=get_thread_info, args=(number,))
thread2 = threading.Thread(target=get_thread_info, args=(number,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
