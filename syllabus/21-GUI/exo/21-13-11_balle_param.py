from tkinter import *

# les variables suivantes seront utilisées de manière globale :
x1, y1 = 150, 150 # coordonnées initiales

# procédure générale de déplacement :
def avance(gd, hb):
    global x1, y1
    x1, y1 = x1 +gd, y1 +hb
    can1.coords(oval1, x1, y1, x1+30, y1+30)

# gestionnaires d'événements :
# le saut de la balle n'est plus une constante, mais une valeur lue dans l'entry
def depl_gauche():
    avance(-int(e.get()), 0)

def depl_droite():
    avance(int(e.get()), 0)
    
def depl_haut():
    avance(0, -int(e.get()))
    
def depl_bas():
    avance(0, int(e.get()))

#------ Programme principal -------
    
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec Tkinter")

# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=300,width=300)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
can1.pack(side=LEFT)

# Boutons principaux 
Button(fen1,text='Quitter',command=fen1.destroy).pack(side=BOTTOM)
Button(fen1,text='Gauche',command=depl_gauche).pack()
Button(fen1,text='Droite',command=depl_droite).pack()
Button(fen1,text='Haut',command=depl_haut).pack()
Button(fen1,text='Bas',command=depl_bas).pack()

# Nouveauté : la paramètre du "saut" de la balle"
# par défaut : 30 pixels
Label(text="saut:").pack()
e = Entry(fen1, width=5)
e.insert(END, '30')
e.focus_set() # mettre le curseur de la souris dans cet entry
e.pack()

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

