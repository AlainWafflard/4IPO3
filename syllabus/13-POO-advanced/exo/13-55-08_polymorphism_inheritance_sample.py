from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("I am a {}. My name is {}. I am {} years old.".format( self.type, self.name, self.age ))

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    type = "cat"

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    type = "dog"

    def make_sound(self):
        print("Bark")


animal_l = [ Cat("Kitty", 2.5), Dog("Fluffy", 4) ]

for animal in animal_l:
    animal.make_sound()
    animal.info()
    animal.make_sound()