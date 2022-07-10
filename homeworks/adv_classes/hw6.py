        # 1.
        # class Laptop:
        #     """
        #     Make the class with composition.
        #     """
        # class Battery:
        #     """
        #     Make the class with composition.
        #     """
class Laptop:
    def __init__(self):
        battery = Battery('Capacity of battery')
        self.batteries = battery

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

laptop_1 = Laptop()
print(laptop_1.batteries.capacity)


        # 2.
        # class Guitar:
        #     """
        #     Make the class with aggregation
        #     """
        # class GuitarString:
        #     """
        #     Make the class with aggregation
        #     """
class Guitar:
    def __init__(self, guitarsrings):
        self.guitarsrings = guitarsrings

class GuitarString:
    def __init__(self, guitarsrings):
        self.guitarsrings = guitarsrings

guitar = Guitar(0)
guitarsrings = GuitarString(7)


        # 3
        # class Calc:
        #     """
        #     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
        #     Note: this method should be static
        #     """
class Calc:
    @staticmethod
    def add_nums(param_1, param_2, param_3):
        return param_1 + param_2 + param_3

print(f"Calc sum = {Calc.add_nums(2,5,3)}")


        # 4*.
        # class Pasta:
        #     """
        #     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
        #     It should have 2 methods:
        #     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
        #     which should create Pasta instances with predefined list of ingredients.
        #     Example:
        #         pasta_1 = Pasta(["tomato", "cucumber"])
        #         pasta_1.ingredients will equal to ["tomato", "cucumber"]
        #         pasta_2 = Pasta.bolognaise()
        #         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
        #     """
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(ingredients=['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(ingredients=['bacon', 'parmesan', 'eggs'])

carbonara = Pasta.carbonara()
print(f"Ingredients of carbonara {carbonara.ingredients}")

bolognaise = Pasta.bolognaise()
print(f"Ingredients of bolognaise {bolognaise.ingredients}")


        # 5*.
        # class Concert:
        #     """
        #     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
        #     In case of setting visitors_count - max_visitors_num should be checked,
        #     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
        #     Example:
        #         Concert.max_visitor_num = 50
        #         concert = Concert()
        #         concert.visitors_count = 1000
        #         print(concert.visitors_count)  # 50
        #     """
class Concert:
    max_visitor_num = 50

    def __int__(self, visitors_count):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > self.max_visitor_num:
            self._visitors_count = self.max_visitor_num
        else:
            self._visitors_count = value

concert_1 = Concert()
concert_1.visitors_count = 700
print(f"concert_1.visitors_count = {concert_1.visitors_count}")


        # 6.
        # class AddressBookDataClass:
        #     """
        #     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
        #     """
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

contact_1 = AddressBookDataClass(key=1,
                               name="Taras",
                               phone_number="23876108173",
                               address="Lviv",
                               email="taras@email.com",
                               birthday="1.01.1000",
                               age=15)

print(contact_1)


        # 7.
        # Create the same class (6) but using NamedTuple
from collections import namedtuple

AddressBookDataClass = namedtuple("AddressBookDataClass",
                                  ["key",
                                   "name",
                                   "phone_number",
                                   "address",
                                   "email",
                                   "birthday",
                                   "age"])

contact_2 = AddressBookDataClass(1,
                                 "Sergiy",
                                 "98412765481",
                                 "Kyiv",
                                 "sergiy@email.com",
                                 "2.02.2000",
                                 17)
print(contact_2)


        # 8.
        # class AddressBook:
        #     """
        #     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
        #     Make its str() representation the same as for AddressBookDataClass defined above.
        #     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
        #     """
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"AddressBook(key='{self.key}', " \
               f"name='{self.name}', " \
               f"phone_number='{self.phone_number}', " \
               f"address='{self.address}', " \
               f"email='{self.email}', " \
               f"birthday='{self.birthday}', " \
               f"age='{self.age}')"

address_book = AddressBook(1,
                          "Sergiy",
                          "98412765481",
                          "Kyiv",
                          "sergiy@email.com",
                          "2.02.2000",
                          17)

print(address_book)


        # 9.
        # class Person:
        #     """
        #     Change the value of the age property of the person object
        #     """
        #     name = "John"
        #     age = 36
        #     country = "USA"
class Person:
    name = "John"
    age = 36
    country = "USA"

print(f"First age of Person: {Person.age}")

setattr(Person, 'age', '26')
print(f"Changed age of Person: {Person.age}")


        # 10.
        # class Student:
        #     """
        #     Add an 'email' attribute of the object student and set its value
        #     Assign the new attribute to 'student_email' variable and print it by using getattr
        #     """
        #     id = 0
        #     name = ""
        #
        #     def __init__(self, id, name):
        #         self.id = id
        #         self.name = name
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

setattr(Student, 'email', 'student@email.com')
print(f"Attributes email: {Student.email}")

student_email = getattr(Student, 'email')
print(f"Variables email: {student_email}")


        # 11*.
        # class Celsius:
        #     """
        #     By using @property convert the celsius to fahrenheit
        #     Hint: (temperature * 1.8) + 32)
        #     """
        #     def __init__(self, temperature=0):
        #         self._temperature = temperature
        #
        #
        # # create an object
        # {obj} = ...
        #
        # print({obj}.temperature)
class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return (self._temperature * 1.8) + 32

room = Celsius(29)
print(f"In Celsius: {room._temperature}")
print(f"In Fahrenheit: {room.fahrenheit}")
