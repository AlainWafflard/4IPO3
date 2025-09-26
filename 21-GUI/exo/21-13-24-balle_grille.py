from tkinter import *

#------ Classe Balle

class Balle:
    def __init__(self, window, x1=135, y1=135, row=1, column=1 ):
        # x1, y1 = 150, 150 # coordonnées initiales
        self.x1 = x1
        self.y1 = y1
        self.fen = window

        # création du canevas 
        self.can1 = Canvas( self.fen, bg='dark grey', height=300, width=300 )
        self.oval1 = self.can1.create_oval( self.x1, self.y1, self.x1+30, self.y1+30, width=2, fill='red')
        self.can1.grid( row=row, column=column )

    # procédure générale de déplacement :
    def avance(self, gd, hb):
        self.x1 = self.x1 + gd
        self.y1 = self.y1 + hb
        self.can1.coords(self.oval1, self.x1, self.y1, self.x1+30, self.y1+30)

    # gestionnaires d'événements :
    def depl_gauche(self):
        self.avance(-10, 0)

    def depl_droite(self):
        self.avance(10, 0)
        
    def depl_haut(self):
        self.avance(0, -10)
        
    def depl_bas(self):
        self.avance(0, 10)

#------ Programme principal -------

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec Tkinter")

# La balle est créée dans la fenêtre
b = Balle(window=fen1, row=1, column=1 )

# On ajoute les widgets
# les callbacks se réfèrent à des méthodes de la balle
Button(fen1,text='Gauche',command=b.depl_gauche).grid( row=1, column=0 )
Button(fen1,text='Droite',command=b.depl_droite).grid( row=1, column=2 )
Button(fen1,text='Haut',command=b.depl_haut).grid( row=0, column=1 )
Button(fen1,text='Bas',command=b.depl_bas).grid( row=2, column=1 )
Button(fen1,text='Quitter',command=fen1.destroy).grid( row=2, column=2 )

# On ajoute la photo en haut à gauche
can2 = Canvas( fen1, width=30, height=30, bg='white' )
photo = PhotoImage(file='programmation.gif')
item = can2.create_image( 15, 15, image=photo )
can2.grid( row=0, column=0, sticky=W )

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

#------ EOF