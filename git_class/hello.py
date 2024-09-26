# This is a sample Python script.

def print_hi(name):
    """
    Salue la personne dont le nom est fourni en paramètre
    :param name: le  nom à afficher
    :return: string avec la salutation
    """
    return f'Hi, {name}'


if __name__ == '__main__':
    print("test module:", __name__)
    print(print_hi('PyCharm'))

    for k in range(10):
        print(k, end="|")
    print()

    print( 2024, 9, 12, sep="/" )

    liste  = [ "a", "b", "c", "d"]
    print(liste[-4])

    try:
        print(liste[-5])
    except:
        print('ya une erreur avec -5')

    print("la suite...")

    liste.append("f")
    print(liste)

    fruit_d = {
        "apple"    : 10,
        "pear"     : 5
    }
    fruit_d["cherry"] = 30
    print(fruit_d)
    print(fruit_d["pear"])

    if "apple" in fruit_d:
        print("ya des pommes")
    if 5 in fruit_d:
        print("il y a 5")

    # print(fruit_d["mango"])
    print(fruit_d.get("mango",0))
    print(fruit_d.get("apple",0))

    for fruit, qnt in fruit_d.items():
        print( fruit, qnt)


