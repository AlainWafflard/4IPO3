
def get_capital(nom):
    cap = float(input(f" Cher.e {nom}, votre capital ? "))
    return cap

def get_taux(nom):
    t = float(input(f" Cher.e {nom}, votre taux ? "))
    return t

####################################################

// print(f" nom du module : {__name__}")

if __name__ == "__main__":
    duree = 5
    name = input(" Votre nom ? ")
    capital = get_capital(name)
    taux = get_taux(name)

    for annee in range(5) :
        capital *= ( 1 + taux/100 )
        print( f"{annee+1} {capital:12.2f}" )

