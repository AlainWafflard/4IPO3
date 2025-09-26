# ce programme associe l'évènement "simple clic" à la fonction hello()
# et l'évènement "double clic" à la fonction quit()

from tkinter import *
import sys 

def hello(event):
    print("Single Click, Button-l") 

def quit(event):                           
    print("Double Click, so let's stop") 
    sys.exit() 

widget = Button(None, text='Mouse Clicks')
widget.pack()

# associations évènement-fonction 
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 

widget.mainloop()
