# Modifier dynamiquement le texte d'un GUI
# Via l'utilisation d'un objet de tkinter appelé "StringVar"

from tkinter import *

w = Tk()

# Entry A 
Label(w, text="A").pack(pady=(40,0))

ea = Entry(w, width=15 )
ea.insert(END, 'texte à copier')
ea.pack()

# Button B
Label(w, text="B").pack(pady=(40,0))

b_sv = StringVar()
b_sv.set("button")
bb = Button(w, textvariable=b_sv, width=15)
bb.pack()

# Label D
Label(w, text="D").pack(pady=(40,0))

c_sv = StringVar()
c_sv.set("label")
lc = Label(w, textvariable=c_sv, bg="gray", fg="whitesmoke", width=15)
lc.pack()

# créer un bouton dont l'évènement (le clic)
# copie le contenu de A dans B et dans C 
def b_callback():
    value = ea.get()
    b_sv.set( value )
    c_sv.set( value )

b = Button(w, text="copy A in B and D", width=15, command=b_callback)
b.pack(pady=(40,0))

w.mainloop()
