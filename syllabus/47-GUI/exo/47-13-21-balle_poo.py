import tkinter as tk


class Balle:
    """ Classe Balle """
    def __init__(self, x1=150, y1=150 ):
        # Création du widget principal ("maître") :
        self.win = tk.Tk()
        self.win.title("Exercice d'animation avec Tkinter")

        # x1, y1 = 150, 150 # coordonnées initiales
        self.x1 = x1
        self.y1 = y1

        # création des widgets "esclaves" :
        self.can1 = tk.Canvas( self.win, bg='dark grey', height=300, width=300 )
        self.oval1 = self.can1.create_oval( self.x1, self.y1, self.x1+30, self.y1+30, width=2, fill='red')
        self.can1.pack(side=tk.LEFT)

        # On ajoute les widgets
        # les callbacks se réfèrent à des méthodes de la balle
        tk.Button(self.win, text='Quitter', command=self.win.destroy).pack(side=tk.BOTTOM)
        tk.Button(self.win, text='Gauche', command=self.depl_gauche).pack()
        tk.Button(self.win, text='Droite', command=self.depl_droite).pack()
        tk.Button(self.win, text='Haut', command=self.depl_haut).pack()
        tk.Button(self.win, text='Bas', command=self.depl_bas).pack()

        # paramètre du "saut" de la balle" (par défaut : 30 pixels)
        tk.Label(text="saut:").pack()
        self.e = tk.Entry(self.win, width=5)
        self.e.insert(tk.END, '30')
        self.e.focus_set()  # mettre le curseur de la souris dans cet entry
        self.e.pack()

    # procédure générale de déplacement :
    def avance(self, gd, hb):
        self.x1 = self.x1 + gd
        self.y1 = self.y1 + hb
        self.can1.coords(self.oval1, self.x1, self.y1, self.x1+30, self.y1+30)

    # gestionnaires d'événements :
    # le saut de la balle n'est plus une constante, mais une valeur lue dans l'entry
    def depl_gauche(self):
        self.avance(-int(self.e.get()), 0)

    def depl_droite(self):
        self.avance(int(self.e.get()), 0)
        
    def depl_haut(self):
        self.avance(0, -int(self.e.get()))
        
    def depl_bas(self):
        self.avance(0, int(self.e.get()))

    # démarrage du réceptionnaire d'évènements (boucle principale) :
    def mainloop(self):
        self.win.mainloop()


if __name__ == "__main__":
    # La balle est créée dans la fenêtre avec ses widgets
    ma_balle = Balle()

    # démarrage du réceptionnaire d'évènements (boucle principale) :
    ma_balle.mainloop()

