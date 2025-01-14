import tkinter
import sqlite3
import sys
from tkinter import ttk

######################################################################
# ouvrir et fermer la connexion à la base de données -----------------

def db_open():
    try:
        db = "scoring_sqlite.db"
        con = sqlite3.connect(db)
        return con

    except Exception as error:
        print("ERROR : while connecting to database : " + str(error))
        print("DEBUG : dsn = " + PATH + database)
        con.close()
        sys.exit()

def db_close(con):
    # Closing the connection
    con.close()

######################################################################
# définition du GUI --------------------------------------------------

def gui_init():
    # ouvrir une fenêtre = création d'un objet appelé ici "window"
    w = tkinter.Tk()

    l = tkinter.Label(w, text="nom de la table:", width=15)
    l.grid(row=0, column=0)  # affichage

    # créer une "entry" càd un emplacement pour introduire une donnée sur une ligne
    e = tkinter.Entry(w)
    e.insert(0, "player_score_partie")
    e.grid(row=0, column=1)  # affichage
    e.config(state='disabled')
    # e.focus_set()  # mettre le curseur de la souris dans cet entry

    # créer un bouton
    # b = tkinter.Button(w, text="afficher", width=10,
    #                    command=lambda: callback(window, e, conn))
    # b.grid(row=0, column=2)

    # obligatoire : faire tourner une fonction qui permet au programme de
    # rester à l'écoute des événéments.
    # sans cette fonction, le programme se termine et le GUI est mort.
    # window.mainloop()
    return w


######################################################################
# création d'un affichage de type "TreeView"

def display_treeview(w, conn):

    def fixed_map(option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.
        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in style.map('Treeview', query_opt=option) if
                elm[:2] != ('!disabled', '!selected')]

    # définir un style pour cette tree_view
    style = ttk.Style()
    style.map('Treeview',
              foreground=fixed_map('foreground'),
              background=fixed_map('background'))
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 10))  # Modify the font of the body
    style.configure("Treeview.Heading", font=('Calibri', 14, 'bold'))  # Modify the font of the headings
    style.layout("Treeview", [('tv.treearea', {'sticky': 'nsew'})])  # Remove the borders

    # create and locate Treeview with 3 columns
    cols = ('la partie', 'le joueur', 'le score')
    tree_view = ttk.Treeview(w, columns=cols, show='headings', style="Treeview")
    tree_view.grid(row=1, column=0, columnspan=3)

    # set column headings
    for col in cols:
        tree_view.heading(col, text=col.upper())  # afficher titre colonne en majuscule
        tree_view.column(col, anchor=tkinter.E)   # aligner le contenu  à droite

    # query
    sql_s = """
        SELECT partie, name, score
        FROM player_score_partie
        ORDER BY score DESC
        LIMIT 5;
    """
    cur = conn.cursor()  # Create a Cursor object
    cur.execute(sql_s)
    result = cur.fetchall()

    # display data in columns
    for i, t in enumerate(result):
        bg = "even" if i % 2 else "odd"
        tree_view.insert("", "end", values=t, tags=(bg,))

    # lignes de couleur alternée
    tree_view.tag_configure('odd', background='#EEEEEE')
    tree_view.tag_configure('even', background='#CCCCCC')


######################################################################
# MAIN

connexion = db_open()
window = gui_init()
display_treeview(window, connexion) # afficher la table
db_close(connexion)
window.mainloop()

# EOF