from abc import ABC, abstractmethod


class Animal(ABC):
    _family = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a {self._family}. My name is {self.name}. I am {self.age} years old.")

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    _family = "cat"

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    _family = "dog"

    def make_sound(self):
        print("Bark")


animal_l = [ Cat("Kitty", 2.5), Dog("Fluffy", 4) ]

for animal in animal_l:
    animal.make_sound()
    animal.info()
    animal.make_sound()

