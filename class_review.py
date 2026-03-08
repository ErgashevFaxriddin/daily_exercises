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


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old.")


s1 = Student("Sara", 20)
s1.introduce()