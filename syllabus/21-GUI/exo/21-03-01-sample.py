# importer le module tkinter
from tkinter import *

# ouvrir une fenêtre = création d'un objet appelé ici "window"
window = Tk()
#
# set your favourite rgb color, eg. Magenta
# https://www.w3schools.com/colors/colors_names.asp
mycolor1 = '#{:02x}{:02x}{:02x}'.format(255, 0, 255)
print(mycolor1)
mycolor2 = '#00FFFF'
mycolor3 = 'Magenta'
window.configure(bg=mycolor2)

# créer une "entry" càd un emplacement pour introduire une donnée sur une ligne 
e = Entry(window)
e.pack()  # affichage
e.focus_set()  # mettre le curseur de la souris dans cet entry

# créer une zone pour afficher du texte 
t = Text(window, height=5, width=20)
t.pack()


# définir la commande (callback) pour le bouton, càd :
# - reproduire le contenu de e dans t
# - effacer le contenu de e 
def b_callback():
    user_str = e.get()
    print(user_str)
    t.insert(END, user_str + "\n")
    e.delete(0, END)


# créer un bouton 
b = Button(window, text="get", command=b_callback )
b.pack()

# obligatoire : faire tourner une méthode qui permet au programme de
# rester à l'écoute des événements.
# sans cette fonction, le programme se termine et le GUI est mort.
window.mainloop()

# fermer la fenêtre, quand l'utilisateur en a terminé avec l'interaction
# window.destroy()
