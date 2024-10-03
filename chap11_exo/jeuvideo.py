class JeuVideo:
    device = "screen"

    def __init__(self, name, dim, price, min_age):
        """
        constructeur
        :param name:
        :param dim:
        :param price:
        :param min_age:
        """
        self.name = name
        self.dim  = dim
        self.price  = price
        self.min_age = min_age
        # self.device = "screen"

    def __str__(self):
        """ retourne les specs du jeu video """
        return f"name:{self.name} ; price:{self.price}"

    def __repr__(self):
        return f"{self.name};{self.dim};{self.price};{self.min_age}"

    def print_spec(self):
        """ imprime les specs du jeu video """
        print( f"name:{self.name} ; price:{self.price}")

################################################################


if __name__ == "__main__":
    jeu1_o = JeuVideo( "Tetris", 2, 0, 5 )
    print(jeu1_o.name)
    print(jeu1_o.price)
    jeu2_o =  jeu1_o
    jeu1_o.print_spec()
    jeu2_o.print_spec()

    jeu1_o.price = 10
    jeu1_o.print_spec()
    jeu2_o.print_spec()

    jeu3_o = JeuVideo( "Tetris", 2, 0, 5 )

    print(jeu1_o)
    out = str(jeu3_o)       # int() float()
    print(out)

    print(jeu1_o == jeu2_o)
    print(jeu1_o == jeu3_o)

    csv = repr(jeu3_o)
    print(csv)



    # x = 4
    # y = x
    # print(x, y )
    # x = 5
    # print(x, y )

    # print(jeu1_o)
    # print(jeu2_o)
