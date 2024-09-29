
# Basic Class

class Car:
	def __init__(self,brand , model):
		self.brand= brand
		self.model= model

	def full_name(self):
		return (f"This is a {self.brand} {self.model}")


Toyata = Car("Toyota" , "Foruner")

print(Toyata.brand)
print(Toyata.model)

print(Toyata.full_name())