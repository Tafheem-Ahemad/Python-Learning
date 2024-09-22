# Question 4

def area(a : int, b :int) -> str:
	return a+b

print(area(10,20))
# print(area("Ahemad",20)) #It give error because we are passing string value instead of integer value.

# Question 5
def name(s : str) -> str:
	return f"my name is {s}"

print(name("Ahemad"))

# Question 6
def my_name(s = "User") -> str:
	return f"my name is {s}"

print(my_name("Ahemad"))
print(my_name())