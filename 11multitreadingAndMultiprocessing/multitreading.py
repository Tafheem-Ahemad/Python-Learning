import threading
import time

def print_number():
	for i in range(1,5):
		time.sleep(1)
		print(i)

def print_letters():
	for it in "Kalix":
		time.sleep(1)
		print(it)

t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letters)

# Start the Threads
t1.start()
t2.start()

# Join with the main Thread
t1.join()
t2.join()

print("The Work is complited")