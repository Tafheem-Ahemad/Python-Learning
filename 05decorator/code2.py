
def debuger(func):
	def wrapper(*args,**kwargs):
		args_value = ", ".join(str for str in args)
		result = func(*args,**kwargs)
		print(f"calling: {func.__name__} with args {args_value}")
		return result
	return wrapper


@debuger
def f1(first_name , last_name="Ahemad"):
	return (f"{first_name} {last_name}")


print(f1("Tafheem","Ahemad"))
