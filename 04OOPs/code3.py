# Static Methods

class Car:

	__total_counts =0

	def __init__(self,brand:str , model:str):
		self.__brand= brand
		self.__model= model
		Car.__total_counts+=1

	def get_brand(self):
		return self.__brand
	def get_model(self):
		return self.__model
	
	
	def full_name(self):
		return f"This is {self.__brand} {self.__model}"
	
	@staticmethod
	def get_total_count():
		return Car.__total_counts
	
	@property
	def model(self):
		return self.__model

class ElectricCar(Car) :
	def __init__(self,brand : str , model : str , power :int):
		super().__init__(brand, model)
		self.__power = power


	def get_power(self):
		return self.__power

	def full_name(self):
		return f"This is {self.get_brand()} {self.get_model()} with {self.__power} power"
	

Tesla = ElectricCar("Tesla","Model X",100)
my_car = Car("Tata" , "Harrier")

# print(Car.__total_counts)
# print(Tesla.__total_counts)

print(Car.get_total_count())
print(Tesla.get_total_count())

### When You "Tesla.get_total_count()" it treats as "Car.get_total_count()"


my_new_car = Car("Land Rover" , "Range Rover")

# Using "property" Decorater so that value will not change
print(my_new_car.get_model())
print(my_new_car.model)  #Model is now work as a property


print(isinstance(Tesla,Car))
print(isinstance(Tesla,ElectricCar))
print(isinstance(my_car,ElectricCar))