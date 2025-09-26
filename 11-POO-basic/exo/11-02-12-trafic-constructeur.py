# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Light :

    def __init__(self):
        self.color = 1

    def change(self):
        self.color += 1
        if( self.color > 3 ):
            self.color = 1

    def __str__(self):
        return "light color is {}".format(self.color)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    feu01 = Light()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)
    feu01.change()
    print(feu01)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
