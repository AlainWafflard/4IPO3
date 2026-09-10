
def f(x: float) -> int:
	y = x/2
	return y  # the editor generates a warning: Expected type 'int', got 'float' instead


print(f(7))
# print(f("hello"))

print(f.__annotations__)

