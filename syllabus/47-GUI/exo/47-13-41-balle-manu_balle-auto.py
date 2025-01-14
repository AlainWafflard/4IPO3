from tkinter import *

#------ Classe Balle

class Logo:
    def __init__(self, window, filename):
        self.can2 = Canvas( window, width=30, height=30, bg='white' )
        self.can2.grid( row=1, column=1, sticky=W )
        self.photo = PhotoImage( file=filename )
        self.item = self.can2.create_image( 15, 15, image=self.photo )

class Balle_manuelle:
    def __init__(self, canevas, x1=10, y1=10 ):
        # x1, y1 = 150, 150 # coordonnées initiales
        self.x1, self.y1 = x1, y1
        self.canevas = canevas
        self.dx, self.dy = 15, 0          # 'pas' du déplacement
        self.oval1 = self.canevas.create_oval( self.x1, self.y1, self.x1+30, self.y1+30, width=2, fill="red" )

    # procédure générale de déplacement :
    def avance(self, gd, hb):
        self.x1 = self.x1 + gd
        self.y1 = self.y1 + hb
        self.canevas.coords(self.oval1, self.x1, self.y1, self.x1+30, self.y1+30)

    # gestionnaires d'événements :
    def depl_gauche(self):
        self.avance(-10, 0)

    def depl_droite(self):
        self.avance(10, 0)
        
    def depl_haut(self):
        self.avance(0, -10)
        
    def depl_bas(self):
        self.avance(0, 10)

class Balle_automatique:
    def __init__(self, canevas, x1=10, y1=10  ):
        # x1, y1 = 150, 150 # coordonnées initiales
        self.x1, self.y1 = x1, y1
        self.canevas = canevas
        self.move_flag = False # commutateur
        self.dx, self.dy = 15, 0          # 'pas' du déplacement
        self.oval1 = self.canevas.create_oval( self.x1, self.y1, self.x1+30, self.y1+30, width=2, fill="green" )

    def start_it(self):
        "démarrage de l'animation"
        if self.move_flag == False :         # pour ne lancer qu'une seule boucle
            self.move_flag = True
        self.move_auto()

    def stop_it(self):
        "arret de l'animation"
        self.move_flag = False

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
        self.canevas.coords(self.oval1,self.x1,self.y1,self.x1+30,self.y1+30)
        # => boucler après 50 millisecondes
        if self.move_flag :
            # self.fen.after(3000,self.move_auto)
            self.canevas.master.after(100,self.move_auto)

#------ Programme principal -------

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec Tkinter")

# On ajoute la photo en haut à gauche
# Obligatoire de mettre "l = Logo(...)" sinon l'objet est effacé et
# la photo n'est pas affichée.
l = Logo( window=fen1, filename="programmation.gif" )

# création du canevas 
can = Canvas( fen1, bg='dark grey', height=300, width=300 )
can.grid( row=2, column=2 )

# La balle est créée dans la fenêtre
bm = Balle_manuelle(canevas=can, x1=100, y1=100 )
ba = Balle_automatique(canevas=can, x1=250, y1=250 )

# On ajoute les widgets
# les callbacks se réfèrent à des méthodes de la balle
# Idéalement, ces boutons devraient être créés dans la classe Balle_manuelle
Button(fen1,text='Gauche',command=bm.depl_gauche).grid( row=2, column=1 )
Button(fen1,text='Droite',command=bm.depl_droite).grid( row=2, column=3 )
Button(fen1,text='Haut',command=bm.depl_haut).grid( row=1, column=2 )
Button(fen1,text='Bas',command=bm.depl_bas).grid( row=3, column=2 )

# les mouvements automatiques
# Idéalement, ces boutons devraient être créés dans la classe Balle_automatique
Button( fen1, text='Démarrer', command=ba.start_it).grid( row=1, column=3 )
Button( fen1, text='Arrêter', command=ba.stop_it).grid( row=3, column=1 )

# Pour quitter l'application
Button(fen1,text='Quitter',command=fen1.destroy).grid( row=3, column=3 )

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

#------ EOF ----------------------------------------------------------