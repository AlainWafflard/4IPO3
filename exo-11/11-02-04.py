# la classe C …
class C:
    a = 0
    b = 0
    c = 0

    def test (self):
        a = C.a = 1
        self.a = 10
        C.b = 2
        self.c = 3
        print( a, C.b, C.c )


# le code principal …
O = C()
O.test()
print( C.a, O.a )
print( C.b, O.b )
print( C.c, O.c )

