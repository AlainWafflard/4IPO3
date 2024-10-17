def may_access_to_temperature(name):
    return name=="Karl"


class Thermometre:
    zero_absolu = -273.15

    def __init__(self, val, owner):
        self.__value = val
        self.__owner = owner

    @property
    def value(self):
        if may_access_to_temperature(self.__owner):
            return self.__value
        else:
            return "pas d'accès"

    @value.setter
    def value(self, new_value):
        if may_access_to_temperature(self.__owner):
            if new_value < Thermometre.zero_absolu :
                self.__value = Thermometre.zero_absolu
            else:
                self.__value = new_value
        else:
            pass

    def getdown(self):
        for k in range(10):
            self.value -= 10
            print(self.value)

# MAIN
# print(Thermometre.zero_absolu)
t = Thermometre(50, "Karl")
print( t.value )
t.value = -200
print( t.value )
t.getdown()


u = Thermometre(66, "Pierre")
print( u.value )
u.value = 200
print( u.value )

