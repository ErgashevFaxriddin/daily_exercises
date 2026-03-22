class Pet:
    def __init__(self, name, species):
        self.name = name        # Attribute
        self.species = species  # Attribute

    def speak(self, sound):     # Method
        return f"{self.name} says {sound}!"

# 2. Create the objects
my_dog = Pet("Buddy", "Dog")
my_cat = Pet("Whiskers", "Cat")

# 3. Use the objects
print(my_dog.speak("Woof"))
print(my_cat.speak("Meow"))
