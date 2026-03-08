class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)


p1 = Person("Ali")
p1.say_hello()