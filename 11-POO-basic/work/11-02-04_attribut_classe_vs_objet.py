class C:
	a = 0
	b = 0
	c = 0
	d = -1

	def test (self):
		a = 1  		# cela reste une variable locale car elle n'est liée à rien lors de son affectation
		C.b = 2 	# cela reste un attribut de classe car il est référé comme tel
		self.c = 3 	# cela devient, grâce à la présence de self, un attribut d'objet
		self.d = 4
		print( a, C.b, C.c )


if __name__ == "__main__":
	O = C()
	P = C()
	O.test()
	print( C.a, O.a, P.a )
	print( C.b, O.b, P.b )
	print( C.c, O.c, P.c )
	print(P.d)

