class Light():
    """
    Output :
    light color is 1
    light color is 2
    light color is 3
    light color is 1 ....
    """
    def __init__(self):
        self.color = 0

    def __str__(self):
        return f"light color is {self.color}"

    def change(self):
        self.color += 1
        if self.color > 3 :
            self.color = 1


if __name__ == "__main__":
    feu01 = Light()
    feu01.color = 1
    for _ in range(10):
        print(feu01)
        feu01.change()

