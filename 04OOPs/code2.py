
# Basic Inheritance

# For making it "Private" we mark  it "__name" means "__"
# For making it "Protected" we mark  it "_name" means "_"

# If a method is present in a that class , then it call it , else it search in that parent class

class Car:
	def __init__(self,brand:str , model:str):
		self.__brand= brand
		self.__model= model

	def get_brand(self):
		return self.__brand
	def get_model(self):
		return self.__model

	def full_name(self):
		return f"This is {self.__brand} {self.__model}"


class ElectricCar(Car) :
	def __init__(self,brand : str , model : str , power :int):
		super().__init__(brand, model)
		# Car.__init__(self,brand, model) // This can be write 
		self.__power = power


	def get_power(self):
		return self.__power

	def full_name(self):
		return f"This is {self.get_brand()} {self.get_model()} with {self.__power} power"



Tesla = ElectricCar("Tesla","Model X",100)
my_car = Car("Tata" , "Harrier")

print(Tesla.full_name())
print(my_car.full_name())