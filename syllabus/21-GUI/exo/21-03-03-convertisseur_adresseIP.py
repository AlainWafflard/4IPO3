# importer le module tkinter
from tkinter import *

#
# 1. écrire un programme qui convertit un nombre décimal en binaire
#    exemple : 16 => 00001000
#             255 => 11111111
#              13 => 00001101
#             128 => 10000000
#             127 => 01111111
#             129 => 10000001
#  128 + 64 = 192 => 11000000
#
#   56 = 5 * 10 + 6 (décimal) 
#   101 binaire = 1 * 4 + 0 * 2 + 1 * 1 = 5 décimal
#   1101 binaire = 1*8 + 1*4 + 0*2 + 1*1 = 13 décimal
#   


# 2. écrire le GUI qui exécute ce programme


def convert10to2( dec ):
    """ convertit un nombre décimal en binaire
        param nombre décimal
        return nombre binaire
    """
    if dec > 255 or dec < 0 :
        return False
    bin_l = []
    
    for i in [ 128, 64, 32, 16, 8, 4, 2, 1 ]:
        if dec >= i :
            bin_l.append("1")
            dec = dec - i
        else:
            bin_l.append("0")
    bin_s = "".join(bin_l)

    return bin_s

def convertIPaddress10to2( ip_address ):
    """ convertit une adresse IP (4) en binaire
        param string 193.294.129.7
        return string 11001100.10101010.00001111.0000001
    """
    ip_l = ip_address.split(".")
    ip_bin_l = []
    for ip in ip_l:
        bin = convert10to2(int(ip))
        ip_bin_l.append(bin)
    ip_bin_s = ".".join(ip_bin_l)
    return ip_bin_s 


# définir la commande (callabck) pour le bouton, càd :
# - reproduire le contenu de e dans t
# - effacer le contenu de e 
def cb_convertir(e_ipa_dec, e_ipa_bin):
    ipa_dec = e_ipa_dec.get()
    ipa_bin = convertIPaddress10to2( ipa_dec )
    e_ipa_bin.insert(0,ipa_bin)

########################################################

def gui():
    # ouvrir une fenêtre = création d'un objet appelé ici "window"
    window = Tk()

    # créer une "entry" + bouton 
    e_ipa_dec = Entry(window)
    e_ipa_bin = Entry(window, width=36)
    b = Button(window, text="convertir", command=lambda:cb_convertir(e_ipa_dec,e_ipa_bin ) )

    e_ipa_dec.pack()  # affichage
    e_ipa_dec.focus_set()  # mettre le curseur de la souris dans cet entry
    b.pack()
    e_ipa_bin.pack()  # affichage
    # obligatoire : faire tourner une fonction qui permet au programme de
    # rester à l'écoute des événéments.
    # sans cette fonction, le programme se termine et le GUI est mort.
    window.mainloop()


