from tkinter import *

# create the canvas, size in pixels
canvas = Canvas(width=300, height=200, bg='#0dd3d1')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file
gif1 = PhotoImage(file='programmation.gif')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image=gif1, anchor=NW)

# run it ...
mainloop()

