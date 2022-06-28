
print("# 1. Create a class Vehicle with Attributes: name, max_speed, and total_capacity.\n"
      "# Method: fare. It should calculate the price of the trip.\n"
      "# Formula: total_capacity * 100. Example, total_capacity = 50 => fare = 5000")
class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100

car_test = Vehicle(name='Test', max_speed=120, total_capacity=60)

print("Result fare = " + str(car_test.fare()), "\n")


print("# 2. Create classes Bus and Car that inherit Vehicle.")
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity

    def fare(self):
        extra_fare = super().fare() // 10
        return super().fare() + extra_fare
        # return  self.total_capacity * 100 + extra_fare

    def check_capacity(self):
        if self.used_capacity > self.total_capacity:
            return "Error"
        elif self.used_capacity < self.total_capacity:
            return "Good"

    def __len__(self):
        return len(self.name)

bus_test = Bus(name='Test', max_speed=120, total_capacity=90, used_capacity=95)

class Car(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

print("Done\n")


print("# 3. Create 3 car objects and 2 bus objects")
car_1 = Car(name='Subaru', max_speed=190, total_capacity=6)
car_2 = Car(name='Audi', max_speed=220, total_capacity=5)
car_3 = Car(name='Toyota', max_speed=180, total_capacity=7)

bus_1 = Bus(name='Man', max_speed=120, total_capacity=90, used_capacity=70)
bus_2 = Bus(name='Ford', max_speed=130, total_capacity=80, used_capacity=60)

print("Done\n")


print("# 4. Check: if car_1 is instance of Car.\n"
      "# if car_2 is instance of Vehicle.\n"
      "# if bus_1 is instance of Car.\n"
      "# if bus_1 is instance of Vehicle.")
print(isinstance(car_1, Car))
print(isinstance(car_2, Vehicle))
print(isinstance(bus_1, Car))
print(isinstance(bus_1, Vehicle), "\n")


print("# 5. Override fare method for Bus class.\n"
      "# Here we need to add an extra 10% to the fare.\n"
      "# Formula: total_fare + 10% of total_fare.\n"
      "# Example, fare = 50 => total_fare = 5500")
print("Result fare + 10% = " + str(bus_test.fare()), "\n")


print("# 6. Add used_capacity attribute for Bus.\n"
      "# It means how many people are on the bus.\n"
      "# If used_capacity > total_capacity raise an error.")
print("Result check_capacity = " + str(bus_test.check_capacity()), "\n")


print("# 7. Write a magic method to Bus that would be triggered when len() function is called.\n"
      "# To figure out what magic method you should implement, take a look at the full list of magic methods:\n"
      "# https://www.tutorialsteacher.com/python/magic-methods-in-python.\n"
      "# Play around with other dunder methods")
print(f"Length of name = {len(bus_test)}")
print("")


print("# 8. Create class Engine with attribute volume and method get_volume() that will return volume.")
class Engine(Car):
    def __init__(self, volume, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.volume = volume

    def get_volume(self):
        return self.volume

car_test2 = Engine(volume=10, name='Test2', max_speed=120, total_capacity=6)
print("Result get_volume = " + str(car_test2.get_volume()), "\n")


print("# 9. Inherit Engine by Car class.")
print("Done\n")


print("# 10. Check what is inheritance order of the Car class")
print(Car.__dict__)
print(Car.mro())

