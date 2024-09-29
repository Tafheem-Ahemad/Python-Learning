
name = "Tafheem Ahemad"

def fuc1():
	name= "Alim Ahemad"
	print(name)


fuc1()
print(name)

x=100
def fun2():
	global x
	x=200

print(x)
fun2()
print(x)

# Closure in Python , It is wotk as JavaScript
def f1(num):
	def f2(x):
		return num ** x
	return f2
	
number1  = f1(2)
number2  = f1(3)

print(number1(2))
print(number2(2))