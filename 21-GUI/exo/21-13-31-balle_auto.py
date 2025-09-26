from tkinter import *

#------ Classe Balle

class Balle:
    def __init__(self, window, x1=10, y1=10,  ):
        # x1, y1 = 150, 150 # coordonnées initiales
        self.x1, self.y1 = x1, y1
        self.fen = window
        self.flag = 0 # commutateur
        self.dx, self.dy = 15, 0          # 'pas' du déplacement

        # création du canevas 
        self.can1 = Canvas( self.fen, bg='dark grey', height=300, width=300 )
        self.oval1 = self.can1.create_oval( self.x1, self.y1, self.x1+30, self.y1+30, width=2, fill='green')
        self.can1.grid( row=2, column=2 )

    # procédure générale de déplacement :
    def avance(self, gd, hb):
        self.x1 = self.x1 + gd
        self.y1 = self.y1 + hb
        self.can1.coords(self.oval1, self.x1, self.y1, self.x1+30, self.y1+30)

    # gestionnaires d'événements :
    def start_it(self):
        "démarrage de l'animation"
        if self.flag==0 :         # pour ne lancer qu'une seule boucle
            self.flag=1
        self.move_auto()

    def stop_it(self):
        "arret de l'animation"
        self.flag = 0

    def move_auto(self):
        "déplacement de la balle"
        self.x1, self.y1 = self.x1 + self.dx, self.y1 + self.dy
        if self.x1 >260:
            self.x1, self.dx, self.dy = 260, 0, 15
        if self.y1 >260:
            self.y1, self.dx, self.dy = 260, -15, 0
        if self.x1 <10:
            self.x1, self.dx, self.dy = 10, 0, -15
        if self.y1 <10:
            self.y1, self.dx, self.dy = 10, 15, 0
        self.can1.coords(self.oval1,self.x1,self.y1,self.x1+30,self.y1+30)
        # => boucler après 50 millisecondes
        if self.flag >0:
            self.fen.after(50,self.move_auto)         

#------ Programme principal -------

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec Tkinter")

# La balle est créée dans la fenêtre
b = Balle(window=fen1)

# On ajoute les widgets
# les callbacks se réfèrent à des méthodes de la balle
# les mouvements automatiques
Button( fen1, text='Démarrer', command=b.start_it).grid( row=1, column=3 )
Button( fen1, text='Arrêter', command=b.stop_it).grid( row=3, column=1 )

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

#------ EOF