import multiprocessing
import time

def print_number():
	for i in range(1,5):
		time.sleep(1)
		print(i)

def print_letters():
	for it in "Kalix":
		time.sleep(1)
		print(it)


if __name__ == "__main__" :
	p1=multiprocessing.Process(target=print_number)
	p2=multiprocessing.Process(target=print_letters)

	t1=time.time()
	p1.start()
	p2.start()

	p1.join()
	p2.join()
	t2=time.time()

	print(f"The time is taken is {t2-t1}")