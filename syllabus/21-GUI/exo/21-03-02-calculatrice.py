# importer le module tkinter
from tkinter import *

###########
# callback
def b1_callback():
    line.insert(END, "1" )

def b2_callback():
    line.insert(END, "2" )

def b3_callback():
    line.insert(END, "3" )

def b4_callback():
    line.insert(END, "4")

def bplus_callback():
    line.insert(END, "+" )

def bequal_callback():
    """ La ligne est supposée être de la forme "123+456+789".
        Le calcul est effectué en découpant la ligne suivant le signe "+"
        puis en additionnant les nombres ainsi déterminés.
        Bien entendu, le moindre signe différent de "+" rend cette fonction
        caduque. Par contre, l'utilisateur peut entrer des valeurs au clavier
        autres que 1, 2 ou 3.
    """
    global line 
    user_calculus = line.get()
    user_list_s = user_calculus.split("+")
    # somme = sum(user_list_s)  # KO car ce sont des strings
    # on convertit la liste des strings en integer
    user_list_i = ([int(i) for i in user_list_s])
    somme = sum(user_list_i)
    line.insert(END, "=" + str(somme) )

def bc_callback():
    global line
    line.delete(0,END)

###############################################
# création de l'interface-utilisateur 
w = Tk()

# t = Text(w, height=1, width=20)
line = Entry(w)
line.pack()

b1 = Button(w, text="1", width=2, command=b1_callback )
b1.pack(side=LEFT)

b2 = Button(w, text="2", width=2, command=b2_callback )
b2.pack(side=LEFT)

b3 = Button(w, text="3", width=2, command=b3_callback )
b3.pack(side=LEFT)

b4 = Button(w, text="4", width=2, command=b4_callback)
b4.pack(side=LEFT)

bc = Button(w, text="C", width=2, command=bc_callback )
bc.pack(side=RIGHT)

bequal = Button(w, text="=", width=2, command=bequal_callback )
bequal.pack(side=RIGHT)

bplus = Button(w, text="+", width=2, command=bplus_callback )
bplus.pack(side=RIGHT)

w.mainloop()
