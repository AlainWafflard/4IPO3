
class NokiaPhone:
    marque = "Nokia"

    def __init__(self, s, p):
        """ Constructeur """
        self.serie = s
        self.poids = p

    def __del__(self):
        print("un nokia est détruit")

    def __str__(self):
        return f" Smartphone de marque {self.marque} ; série : {self.serie} "

    def __repr__(self):
        return f"{self.marque};{self.serie};{self.poids}"


if __name__ == "__main__" :
    nokia_kim = NokiaPhone(  "170", 100 )
    print(nokia_kim)
    # print("poids = ", nokia_kim.poids)

    nokia_jim = NokiaPhone(  "180", 150 )
    print(nokia_jim)

    nokia_charles = NokiaPhone(  "170", 100 )
    print(nokia_charles)

    print( nokia_kim == nokia_jim )
    print( nokia_kim == nokia_charles )

    nokia_siegfried = nokia_kim
    print(nokia_siegfried)

    for o in [ nokia_kim, nokia_jim, nokia_charles ]:
        print(repr(o))

