
import time

def cache(func):
	cache_value = {}
	print(cache_value)
	def wrapper(*args):
		if args in cache_value:
			return cache_value[args]
		result = func(*args)
		cache_value[args]=result
		return result
	return wrapper
	
@cache
def add_two_number(a,b):
	time.sleep(2)
	return a+b


print(add_two_number(2,3))
print(add_two_number(2,3))
print(add_two_number(5,3))