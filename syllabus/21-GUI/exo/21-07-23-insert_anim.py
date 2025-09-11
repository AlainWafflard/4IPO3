""" How to play animated GIF ? """

from tkinter import *      
root = Tk()      

def animate(ind=0):
    global img2, canvas
    frame = frame2[ind]
    ind += 1
    img2.configure(image=frame)
    root.after(500, animate, ind)

# Loop through the index of the animated gif
nb_frame = 11
frame2 = [PhotoImage(file='tenor.gif', format = 'gif -index %i' %i) for i in range(nb_frame)]

img2 = Label(root)
img2.pack()

# root.after(0, update, 0)
animate(0)

button1 = Button(root,text = 'Animate', command=animate)
button1.pack()

root.mainloop()

