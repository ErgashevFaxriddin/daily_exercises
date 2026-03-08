# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hello(self):
#         print("Hello, my name is", self.name)
#
#
# p1 = Person("Ali")
# p1.say_hello()

#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print("My name is", self.name, "and I am", self.age, "years old.")
#
#
# s1 = Student("Sara", 20)
# s1.introduce()

#
# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#     def car_info(self):
#         print("This car is", self.brand, "made in", self.year)
#
#
# c1 = Car("Toyota", 2020)
# c1.car_info()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r1 = Rectangle(5, 4)
print("Area:", r1.area())