

# Operator Overloading
# In phython magic methods are used to overload the operators , not like other languages where we have to define the operator overloading functions.



class Vector:
	def __init__(self,x,y) -> None:
		self.x=x;
		self.y=y

	def __add__(a,b):
		return Vector(a.x+b.x,a.y+b.y)
	
	def __mul__(a,b): # *
		return Vector(a.x*b.x,a.y*b.y)

	def __sub__(a,b): # -
		return Vector(a.x-b.x,a.y-b.y)

	def __lt__(a,b): # <
		return Vector(a.x<b.x,a.y<b.y)

	def __le__(a,b): # <=
		return Vector(a.x<=b.x,a.y<=b.y)

	def __gt__(a,b): # >
		return Vector(a.x>b.x,a.y>b.y)

	def __ge__(a,b): # >=
		return Vector(a.x>=b.x,a.y>=b.y)


	def __mod__(a,b): # %
		return Vector(a.x%b.x,a.y%b.y)	

	def __pow__(a,b): # **
		return Vector(a.x**b.x,a.y**b.y)

	def __eq__(a,b): # ==
		return Vector(a.x==b.x,a.y==b.y)


	def __truediv__	(a,b): # /
		return Vector(a.x/b.x,a.y/b.y)
	
	def __floordiv__(a,b): # //
		return Vector(a.x//b.x,a.y//b.y)
	
	def __repr__(self) -> str:
		return f"This number is {self.x} + j{self.y}"


a1=Vector(10,20)
a2=Vector(40,50)

print(a1)
print(a2)

print(a1+a2)
print(a1*a2)
print(a1-a2)
print(a1<a2)
print(a1<=a2)
print(a1>a2)
print(a1>=a2)
print(a1%a2)
print(a1**a2)
print(a1==a2)
print(a1/a2)
print(a1//a2)
