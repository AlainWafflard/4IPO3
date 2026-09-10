from tkinter import *
import random
import copy


class Model:
	__word_original = [ "B", "O", "N", "J", "O", "U", "R"]

	def __init__(self):
		self.__word = copy.copy(self.__word_original)

	def set_word(self, word):
		self.__word = list(word)

	def get_word(self):
		"""
		Retourne les données sous forme de liste
		"""
		return self.__word

	def transform_word(self, index ):
		code = ord(self.__word[index])
		new_letter = chr(code+1)
		self.__word[index] = new_letter

	def reset_word(self):
		self.__word = copy.copy(self.__word_original)


class View:

	def __init__(self, controller):
		self.window = Tk()

		chaine = Label(self.window)
		chaine.configure(text="Form développé sous MVC")
		chaine.pack(side=LEFT)

		b1 = Button(self.window, text='TEST', command=controller.gui_test)  # référence !
		b1.pack(side=LEFT, padx=3, pady=3)

		b2 = Button(self.window, text='Display', command=controller.gui_display)
		b2.pack(side=LEFT, padx=3, pady=3)

		b3 = Button(self.window, text='Transform', command=controller.gui_transform)
		b3.pack(side=LEFT, padx=3, pady=3)

		b4 = Button(self.window, text='Reset', command=controller.gui_reset)
		b4.pack(side=LEFT, padx=3, pady=3)

		# notez les deux manières d'enregistrer le nouveau mot : par <return> ou par bouton
		self.entree = Entry(self.window)
		self.entree.bind("<Return>", lambda event: controller.gui_set(self.entree.get()))
		self.entree.pack(side=LEFT)
		b5 = Button(self.window, text='Set', command=lambda:controller.gui_set(self.entree.get()))
		b5.pack(side=LEFT, padx=3, pady=3)

		self.text = Text(self.window, height=4, width=20)
		self.text.pack()

	def display_word(self, data):
		str = "/".join(data)
		self.text.insert(END, str + "\n")
		print(str)

	def reset_entree(self):
		self.entree.delete(0, END)

	def mainloop(self):
		self.window.mainloop()


class Controller:

	def __init__(self):
		self.model = Model()
		self.view = View(self)
		self.view.mainloop()

	def gui_test(self):
		print("button TEST pressed")

	def gui_display(self):
		"""
		1) Récupère le contenu de Model
		2) L'envoie à  View pour affichage
		"""
		word_l = self.model.get_word()
		self.view.display_word(word_l)

	def gui_transform(self):
		word_l = self.model.get_word()
		i_alea = random.randrange(len(word_l))
		self.model.transform_word(i_alea)
		print("mot transformé")

	def gui_reset(self):
		self.model.reset_word()
		self.view.reset_entree()
		print("mot resetté")

	def gui_set(self, new_word):
		self.model.set_word(new_word)
		print("mot nouveau introduit")


# programme "principal"
if __name__ == "__main__":
	Controller()

# fin de l'application
