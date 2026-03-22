# class Pet:
#     def __init__(self, name, species):
#         self.name = name        # Attribute
#         self.species = species  # Attribute
#
#     def speak(self, sound):     # Method
#         return f"{self.name} says {sound}!"
#
# # 2. Create the objects
# my_dog = Pet("Buddy", "Dog")
# my_cat = Pet("Whiskers", "Cat")
#
# # 3. Use the objects
# print(my_dog.speak("Woof"))
# print(my_cat.speak("Meow"))


class Pet:
    def __init__(self, name, species, color):
        self.name = name        # Attribute
        self.species = species  # Attribute
        self.color = color      # New attribute

    def speak(self, sound):
        # Returns a sentence with name, species, and color
        return f"{self.name}, a {self.color} {self.species}, says {sound}!"

# Create the objects
my_dog = Pet("Buddy", "Dog", "brown")
my_cat = Pet("Whiskers", "Cat", "white")

# Use the objects
print(my_dog.speak("Woof"))
print(my_cat.speak("Meow"))