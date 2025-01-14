# Une balle manuelle
# Trois balles automatiques
# Collisions gérées entre les quatre balles et les murs

from tkinter import *
from random import *

# Environnement général
class Environment :
    def __init__(self):
        # Création du widget principal ("maître") :
        self.mainw = Tk()
        self.mainw.title("Exercice d'animation avec Tkinter")

        # On ajoute la photo en haut à gauche
        # Obligatoire de mettre "l = Logo(...)" sinon l'objet est effacé et
        # la photo n'est pas affichée.
        self.logo = Logo( window=self.mainw, filename="programmation.gif" )

        # création du canevas 
        self.canevas = Canvas( self.mainw, bg='dark grey', height=300, width=300 )
        self.canevas.grid( row=1, column=1 )
    
        # Les balles sont créées dans la fenêtre
        # balle manuelle
        self.bm = Balle_manuelle(canevas=self.canevas, x1=100, y1=100 )

        # balles automatiques
        self.l_balle = []
        self.l_couleur_balle = [ "blue", "red", "green" ]
        for i in range(3):
            x1 = randint(10, 270 )
            y1 = randint(10, 270 )
            self.l_balle.append(Balle_automatique(canevas=self.canevas, \
                x1=x1, y1=y1, fill=self.l_couleur_balle[i], name="b"+str(i) ))

        # définir les collisions entre toutes les balles
        for b in self.l_balle:
            self.bm.define_environment(b)
            b.define_environment(self.bm)
            for ob in self.l_balle:
                b.define_environment(ob)

        # On ajoute les widgets
        # les callbacks se réfèrent à des méthodes de la balle
        # Idéalement, ces boutons devraient être créés dans la classe Balle_manuelle
        Button(self.mainw,text='Gauche',command=self.bm.depl_gauche).grid( row=1, column=0 )
        Button(self.mainw,text='Droite',command=self.bm.depl_droite).grid( row=1, column=2 )
        Button(self.mainw,text='Haut',command=self.bm.depl_haut).grid( row=0, column=1 )
        Button(self.mainw,text='Bas',command=self.bm.depl_bas).grid( row=2, column=1 )

        # les boutons de commande des balles automatiques
        # Idéalement, ces boutons devraient être créés
        # dans la classe Balle_automatique
        self.dashboard = Frame(self.mainw, relief=SUNKEN)
        self.dashboard.grid(row=0, column=3, rowspan=2, sticky=N )
        for b in self.l_balle:
            Button( self.dashboard, text="start "+b.name, command=b.start_it ).pack()
            Button( self.dashboard, text="stop "+b.name, command=b.stop_it ).pack()

        # Pour quitter l'application
        Button( self.mainw, text='Quitter', command=self.destroy ).grid( row=2, column=3 )

        # démarrage du réceptionnaire d'évènements (boucle principale) :
        self.mainw.mainloop()

    # cloture de l'application
    def destroy(self):
        for b in self.l_balle:
            b.stop_it()
            # print(b.name, "stopped")
        self.canevas.master.after( 1500, self.mainw.destroy )

# Class Logo
class Logo:
    def __init__(self, window, filename):
        self.can2 = Canvas( window, width=30, height=30, bg='white' )
        self.can2.grid( row=0, column=0, sticky=W )
        self.photo = PhotoImage( file=filename )
        self.item = self.can2.create_image( 15, 15, image=self.photo )

# Class "super" Balle
class Balle :
    def define_environment(self, other_ball):
        """ gérer la liste des obstacles susceptibles d'entrer en collision
        """
        if( self.name != other_ball.name ):
            self.l_other_balls.append(other_ball)

    def move(self):
        """ déplacement de la balle """
        self.x0, self.y0 = self.x1, self.y1
        self.x1, self.y1 = self.x1 + self.dx, self.y1 + self.dy

        # détection de collision avec les murs
        self.detect_collision_wall()

        # détection de collision avec l'autre balle
        self.detect_collision_ball()

        # repositionner la balle
        self.canevas.coords(self.oval1,self.x1,self.y1,self.x1+2*self.ray,self.y1+2*self.ray)

    def detect_collision_ball(self):
        for ob in self.l_other_balls:
            sq_dist_2balls = (self.x1 - ob.x1)**2 + (self.y1 - ob.y1)**2
            if sq_dist_2balls < (2*self.ray)**2 :
                self.x1, self.y1 = self.x0, self.y0
                # print("collision")
        
# Class Balle Manuelle 
class Balle_manuelle(Balle):
    def __init__(self, canevas, x1=0, y1=0, color="yellow" ):
        self.step = 10
        self.ray = 15
        # x1, y1 = 150, 150 # coordonnées initiales
        self.x1, self.y1 = x1, y1
        self.canevas = canevas
        self.dx, self.dy = self.step, 0          # 'pas' du déplacement
        self.oval1 = self.canevas.create_oval( self.x1, self.y1, self.x1+2*self.ray, self.y1+2*self.ray, width=2, fill=color )
        self.name = "balle_manuelle"
        # liste des balles susceptibles d'entrer en collision
        self.l_other_balls = []

    # gestionnaires d'événements :
    def depl_gauche(self):
        self.move_manu(-self.step, 0)

    def depl_droite(self):
        self.move_manu(self.step, 0)
        
    def depl_haut(self):
        self.move_manu(0, -self.step)
        
    def depl_bas(self):
        self.move_manu(0, self.step)

    def move_manu(self, gd, hb):
        """ procédure générale de déplacement :
            déplacement manuel de la balle
        """
        self.dx, self.dy = gd, hb
        self.move()
        
    def detect_collision_wall(self):
        """ détection de collision avec les murs,
            methode propre à la balle manuelle
            la balle s'arrête
        """
        if self.x1 > 270:
            self.x1 = 270
        if self.y1 > 270:
            self.y1 = 270
        if self.x1 < 0:
            self.x1 = 0
        if self.y1 < 0:
            self.y1 = 0

# Class Balle Automatique 
class Balle_automatique(Balle):
    def __init__(self, canevas, x1=0, y1=0, fill="green", name="b0" ):
        self.step = randint(2, 10)        # 'pas' du déplacement
        self.ray = 15        # rayon de la balle
        # x1, y1 = 150, 150 # coordonnées initiales
        self.x1, self.y1 = x1, y1
        self.canevas = canevas
        self.move_flag = False # commutateur
        self.dx, self.dy = self.step, 0
        self.oval1 = self.canevas.create_oval( self.x1, self.y1, self.x1+2*self.ray, self.y1+2*self.ray, width=2, fill=fill )
        self.name = name
        # liste des balles susceptibles d'entrer en collision
        self.l_other_balls = []

    def start_it(self):
        """démarrage de l'animation"""
        if self.move_flag == False :         # pour ne lancer qu'une seule boucle
            self.move_flag = True
            self.move_auto()

    def stop_it(self):
        """arret de l'animation"""
        self.move_flag = False

    def move_auto(self):
        """ procédure générale de déplacement :
            déplacement automatique de la balle
            boucler après 50 millisecondes
        """
        self.move()
        if self.move_flag :
            self.canevas.master.after( 25, self.move_auto )

    def detect_collision_wall(self):
        """ détection de collision avec les murs,
            methode propre à la balle automatique
            la balle tourne sur sa droite et continue à avancer
        """
        if self.x1 > 270:
            self.x1, self.dx, self.dy = 270, 0, self.step
        if self.y1 > 270:
            self.y1, self.dx, self.dy = 270, -self.step, 0
        if self.x1 < 0:
            self.x1, self.dx, self.dy = 0, 0, -self.step
        if self.y1 < 0:
            self.y1, self.dx, self.dy = 0, self.step, 0

#------ Programme principal -------
# Lancemement de l'environnement de jeu 
e = Environment()

#------ EOF ----------------------------------------------------------
