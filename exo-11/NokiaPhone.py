
class NokiaPhone:
    brand = "Nokia"

    def __init__(self, model, weight, username ):
        """ constructeur """
        self.model = model
        self.weight = weight
        self.insurance_value = None
        self.username = username

    def __del__(self):
        print(f"phone de {self.username} détruit")

    def __str__(self):
        iv = "inconnue" if self.insurance_value is None else self.insurance_value
        out = f"""
Utilisateur : {self.username}
Marque : {self.brand}
Modèle : {self.model}
Poids  : {self.weight}
Valeur assurée  : {iv}
        """
        return out

    def set_insurance_value(self, new_value=None):
        """ calcule la valeur assurée (soit par défaut, soit avec une valeur donnée en param """
        if new_value is None :
            self.insurance_value = self.weight // 2
        else :
            self.insurance_value = new_value


if __name__ == "__main__":

    phoneArthur = NokiaPhone( "5110", 200, "Arthur" )
    # phoneArthur.print_spec()
    phoneArthur.set_insurance_value()
    # phoneArthur.insurance_value = phoneArthur.weight // interdit, pas bien !
    # phoneArthur.print_spec()

    print(phoneArthur)
    # print( "Poids du phone de Arthur : " + str(phoneArthur.weight) )

    phoneKevin = NokiaPhone( "5110", 200, "Kevin" )
    phoneKevin.set_insurance_value()
    # phoneKevin = phoneArthur !!!!!!!!!!! copie des références, et non des objets
    print(phoneArthur)
    print(phoneKevin)

    phoneKevin.set_insurance_value(75)
    print(phoneArthur)
    print(phoneKevin)

    phoneKevin = None
    print(phoneArthur)
    # phoneKevin.print_spec()

    phoneArthur = None
    print("-- EOS --")


