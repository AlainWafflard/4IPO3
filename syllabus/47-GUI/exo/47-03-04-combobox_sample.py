from tkinter import *
from tkinter import ttk     # enrichir tkinter avec des box nouvelles
                            # par ex le combobox = liste d'éléments
from tkinter.constants import *

# params 
FONT = ("Helvetic", 16)
BG = '#1589A4'
FG = "white"

# créer la fenêtre
window = Tk ()
window.title("Combobox - sample")
window.geometry("700x280")
window.config(background=BG)


####
# combo box definition

# label 
Label (window, text= "choisissez votre QUIZZ", font= FONT, bg=BG, fg=FG).pack()

# combo box callback
def launch_quizz_cb(e=None):
    # On affiche a l'écran la valeur selectionnée
    selected_value = game_select_cb.get()
    output_s.set(selected_value)
    print("sélection : " + selected_value)
    # print("évènement : " + str(e) )

def reset_cb():
    # On affiche à l'écran la valeur de départ
    game_select_cb.current(2)
    launch_quizz_cb()

game_select_cb = ttk.Combobox( window,
                               font=FONT,
                               values=["Belgique","Météo","Les chats"])
game_select_cb.insert(3, "Les chiens")

# valeur par défaut : la 3e ("Les chats")
game_select_cb.current(2)

# appliquer la même police pour toutes les listes des Combo
window.option_add('*TCombobox*Listbox.font', FONT)

# On associe une fonction à l'évènement "sélection d'une valeur" du Combo
game_select_cb.bind("<<ComboboxSelected>>", launch_quizz_cb)

# Placement 
game_select_cb.pack()


####
# affichage des évènements 
Label(window, text= "journal des évènements", font=FONT, bg=BG, fg=FG).pack(pady=(40,0))
output_s = StringVar()
output = Label(window, textvariable=output_s, font= FONT, bg="white", fg="grey", width=15)
output.pack()

b_reset = Button( window, text="Réinitialiser", font=FONT, command=reset_cb )
b_reset.pack(pady=(40,0))

# initialiser le journal
launch_quizz_cb()

####
# afficher et mise en attente d'évènement
window.mainloop()

