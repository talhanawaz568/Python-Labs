class Car:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
	def drive(self):
		print(f"The {self.brand} {self.model} is now driving.")

car1 = Car("Tayota", "Carolla")
car2 = Car("Honda", "Civic")

car1.drive()
car2.drive()

print(f"Car 1 brand: {car1.brand}")
print(f"Car 2 brand: {car2.brand}")

class Car:
	wheels = 4
	def __init__(self,brand, model):
		self.brand = brand
		self.model = model
	def drive(self):
		print(f"The {self.brand} {self.model} is now driving.")
print(f"Number of wheels: {Car.wheels}")

