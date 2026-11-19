class Light():
    """
    Output :
    light color is 1
    light color is 2
    light color is 3
    light color is 1 ....
    """
    color_name_l = (
        "",
        "red",
        "green",
        "orange"
    )
    color_index_d = {
        "red"   : 1,
        "green" : 2,
        "orange": 3,
    }
    duration_l = (
        0,
        30,
        25,
        5
    )

    def __init__(self, name, color_name="red"):
        self.color = self.color_index_d[color_name]
        self.name = name

    def __str__(self):
        color_name = self.color_name_l[self.color]
        duration = self.duration_l[self.color]
        return f"color of light '{self.name}' is {color_name} ({duration} sec)"

    def change(self):
        self.color += 1
        if self.color > 3 :
            self.color = 1


if __name__ == "__main__":
    feu01 = Light( color_name="orange", name="LaChasse" )
    for _ in range(10):
        print(feu01)
        feu01.change()

