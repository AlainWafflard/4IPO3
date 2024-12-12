from abc import ABC, abstractmethod


class Animal(ABC):
    _aname = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        print(f"I am a {self._aname}. My name is {self.name}. I am {self.age} years old.")


class Cat(Animal):
    _aname = "cat"

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    _aname = "dog"

    def make_sound(self):
        print("Bark")


animal_l = [ Cat("Kitty", 2.5), Dog("Fluffy", 4) ]

for animal in animal_l:
    animal.make_sound()
    animal.info()
    animal.make_sound()

