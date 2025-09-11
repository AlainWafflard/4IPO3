# on veut afficher la liste suivante
my_list_data = [ "alpha", "beta", "delta", "gamma", "epsilon" ]

# tkinter
# comment associer un callback à une listbox
# par défaut, listbox n'a pas d'option "command" comme les autres.
from tkinter import *

# 1) définir une fonction callback
# Noter "evt" comme paramètre 
def lb_onselect(evt, sel):
    # Note here that Tkinter passes an event object to onselect()
    global label_selection
    w = evt.widget
    index = int(w.curselection()[0]) #  nous avons l'index
                                     # car la sélection est une liste
                                     # vu que plusieurs sélections sont possibles
    value = w.get(index) # nous avons la valeur
    message = 'index {} : valeur "{}"'.format(index, value)
    print( message )
    # nous affichons la valeur de la listbox dans un label
    sel.config(text=message)

#################

master = Tk()
master.pack_propagate(0)
master.geometry("150x210+400+300") # You want the size of the app to be 500x500
master.resizable(0, 0) # Don't allow resizing in the x or y direction

# 2) définir la zone d'entrée , càd
#    la listbox et son évènement "single click" : <<ListboxSelect>>
#    problème : listbox n'a pas d'option "command" comme les autres.

lb = Listbox(master, width=22)
lb.pack()
for item in my_list_data:
    lb.insert(END, item)

# 3) définir la zone de sortie
Label(master, background="grey", foreground="white", text="Votre sélection : ", width=18).pack()
lb_selection = Label(master, background="yellow", foreground="black", text="", width=18)
lb_selection.pack()
lb.bind('<<ListboxSelect>>', lambda event, sel=lb_selection : lb_onselect(event, sel))

mainloop()
