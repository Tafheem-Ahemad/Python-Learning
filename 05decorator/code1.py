import time
from datetime import datetime as dt
from random import randint

def decorater(func):
	def wrapper (*args,**kwargs):
		print(time.time())
		result = func(*args,**kwargs)
		print(dt.now())
		return result
	return wrapper

@decorater
def add_two_number(a,b):
	return a+b


print(add_two_number(100,200))