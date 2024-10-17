class HtmlPageBuilder:

	def __init__(self):
		self.__structure = []

	def append(self, o ):
		self.__structure.append(o)

	def __str__(self):
		s = """
			<html>
			<head></head>
			<body>
		"""
		for e in self.__structure:
			s += str(e)
		s += """
			</body>
			</html>
		"""
		return s


class HtmlDiv:
	__tag = "div"

	def __init__(self):
		self.__contents = ""

	@property
	def contents(self):
		return self.__contents

	@contents.setter
	def contents(self, s):
		self.__contents = s

	def __str__(self):
		ot = "<" + self.__tag + ">"  # open tag
		ct = "</" + self.__tag + ">" # close tag
		s = ot + self.__contents + ct # <div>...</div>
		return s


# MAIN
html_o = HtmlPageBuilder()
div_o = HtmlDiv()
div_o.contents = "Hello World"
html_o.append(div_o)
print(html_o)

# <html>
# <head></head>
# <body>
# 	<div>Hello World</div>
# </body>
# </html>

