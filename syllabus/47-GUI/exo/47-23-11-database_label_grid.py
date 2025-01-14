import tkinter as tk
import sqlite3
import sys

######################################################################
# ouvrir et fermer la connexion à la base de données -----------------

def db_open():
    try:
        db = "scoring_sqlite.db"
        con = sqlite3.connect(db)
        return con

    except Exception as error :
        print("ERROR : while connecting to database : " + str(error) )
        print("DEBUG : dsn = " + PATH+database )
        con.close()
        sys.exit()

def db_close(con):
    # Closing the connection
    con.close()


######################################################################
# définition du GUI --------------------------------------------------

def gui_init():
    # ouvrir une fenêtre = création d'un objet appelé ici "window"
    w = tk.Tk()

    f = tk.Frame(w, width = 100, height = 30)
    f.pack()
    
    tk.Label(f, text="AFFICHAGE D'UNE TABLE DE BASE DE DONNEES").grid(row=0, column=0 )  # titre général 

    tk.Label(f, text="nom de la table:", width=15).grid(row=1, column=0)  # affichage

    # créer une "entry" càd un emplacement pour introduire une donnée sur une ligne
    e = tk.Entry(f)
    e.insert(0, "player_score_partie")
    e.grid(row=1, column=1)  # affichage
    e.config(state='disabled')

    # obligatoire : faire tourner une fonction qui permet au programme de
    # rester à l'écoute des événéments.
    # sans cette fonction, le programme se termine et le GUI est mort.
    # window.mainloop()
    return w


######################################################################
# juste pour dessiner le tableau à partir de la liste "data"
# on calcule le nombre de lignes et colonnesd à partir de "data"

def draw_table_with_labels(w, titles, data):

    CELL_WIDTH = 80
    CELL_HEIGHT= 30
    NB_ROWS = len(data)
    NB_COLS = len(data[0])
 
    # afficher les titres d'abord 
    head_frame = tk.Frame(w, width = NB_COLS*CELL_WIDTH, height = CELL_HEIGHT)
    head_frame.pack()

    for j in range(NB_COLS):
        l = tk.Label( head_frame, width=CELL_WIDTH, relief="raise", borderwidth=1,
                      text=titles[j], bg="white", font=("bold",) )
        l.place(x=j*CELL_WIDTH, y=0 , width=CELL_WIDTH, height=CELL_HEIGHT)

    # afficher les données ensuite 
    main_frame = tk.Frame(w, width = NB_COLS*CELL_WIDTH, height = NB_ROWS*CELL_HEIGHT)
    main_frame.pack()

    for i in range(NB_ROWS):
        bg = "#EEEEEE" if i % 2 == 0 else "#CCCCCC"
        row_frame = tk.Frame(main_frame, width = NB_COLS*CELL_WIDTH, height = CELL_HEIGHT)
        row_frame.pack()
        for j in range(NB_COLS):
            l = tk.Label(row_frame, width=CELL_WIDTH, relief="raise", borderwidth=1,
                      text=str(data[i][j]), anchor="e", bg=bg)
            l.pack()
            l.place(x=j*CELL_WIDTH, y=0 , width=CELL_WIDTH, height=CELL_HEIGHT)
            # print(i, j)


# création d'un affichage à l'aide de Label et de .grid

def display_query(w, conn):

    # query
    sql_s = """
        SELECT partie, name AS joueur, score 
        FROM player_score_partie
        ORDER BY score DESC
        LIMIT 3;
    """
    cur = conn.cursor()  # Create a Cursor object
    cur.execute(sql_s)
    result = cur.fetchall()

    # afficher le titre des colonnes
    col_titles = ( "partie", "joueur", "score total" )

    # afficher les valeurs capturées dans la requête
    # print( "nombre de lignes de données : " + str(len(result)))
    draw_table_with_labels(w, col_titles, result)
    
    # for i in range(len(result)):
    #    bg = "#EEEEEE" if i % 2 else "#CCCCCC"
    #    tk.Label( w, text=result[i][0], relief=tk.SUNKEN, anchor="e", bg=bg, width=40 ).grid( row=i+3, column=0 )
    #    tk.Label( w, text=result[i][1] ).grid( row=i+3, column=1, sticky="e" )
    #    tk.Label( w, text=result[i][2] ).grid( row=i+3, column=2, sticky="e" )


######################################################################
# MAIN

connexion = db_open()
window = gui_init()
display_query(window, connexion) # afficher la table
db_close(connexion)
window.mainloop()

# EOF