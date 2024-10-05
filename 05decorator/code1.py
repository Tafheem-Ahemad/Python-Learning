import time

def decorater(func):
	def wrapper (*args,**kwargs):
		print(time.time())
		result = func(*args,**kwargs)
		print(time.time())
		return result
	return wrapper

@decorater
def add_two_number(a,b):
	return a+b


print(add_two_number(100,200))