import time
from datetime import datetime as dt
from random import randint

def timer(func):
	def wrapper (*args,**kwargs):
		print(time.time())
		result = func(*args,**kwargs)
		print(dt.now())
		return result
	return wrapper

@timer
def add_two_number(a,b):
	return a+b


print(add_two_number(100,200))