import threading 

def print_numbers(thread_name, start, end):
	"""Prints numbers from start to end. """
	for numbers in range(start, end):
		print(f"{thread_name}: {numbers}")

thread1 = threading.Thread(target=print_numbers, args=("Thread-1",0, 5))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 5, 10))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

