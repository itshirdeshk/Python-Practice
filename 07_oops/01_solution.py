class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are Awesome..."
    
    @property
    def model(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("Toyata", "Corolla")
# print(my_car.brand)
# print(my_car.full_name())
print(my_car.fuel_type())

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
print(my_tesla.fuel_type())

print(isinstance(my_tesla, Car))

print(Car.total_car)

class Battery:
    def batery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.batery_info())
print(my_new_tesla.engine_info())