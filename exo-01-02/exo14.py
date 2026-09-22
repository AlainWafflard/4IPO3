a = [ 1, 2 ]
b = a
print( a, b )
a.append(4)
print( a, b )
print( a == b, a is b )

c = [ 1, 2, 4 ]
print( a, c )
print( a == c, a is c )

