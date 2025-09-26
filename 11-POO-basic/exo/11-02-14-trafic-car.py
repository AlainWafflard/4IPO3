# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Car:

    def __init__(self, brand, speed = 0):
        self.brand = brand
        self.speed = speed

    def increment(self, value=1):
        self.speed += value

    def decrement(self):
        self.speed -= 1

    def __str__(self):
        return "{}: speed {} km/h".format(self.brand, self.speed)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    voiture_A = Car("Peugeot")
    print(voiture_A)
    voiture_A.increment()
    print(voiture_A)
    voiture_A.increment(10)
    print(voiture_A)
    voiture_A.decrement()
    print(voiture_A)

