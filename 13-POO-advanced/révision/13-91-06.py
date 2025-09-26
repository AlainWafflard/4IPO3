class HtmlPageBuilder:

	def __init__(self):
		self._children = []  # attribut protégé car existe aussi dans les classes enfants

	def append(self, o ):
		self._children.append(o)

	def __str__(self):
		structure_s = "".join([str(e) for e in self._children])
		s = """
			<html>
			<head></head>
			<body>
				{}
			</body>
			</html>
		""".format(structure_s)
		return s


class HtmlDiv(HtmlPageBuilder):
	_tag = "div"

	def __init__(self, c=""):
		self.__contents = c
		self._children = []

	@property
	def contents(self):
		return self.__contents

	@contents.setter
	def contents(self, s):
		self.__contents = s

	def __str__(self):
		ot = "<" + self._tag + ">"  # open tag
		ct = "</" + self._tag + ">" # close tag
		# if len(self.__children) > 0:
		structure_s = "".join([str(e) for e in self._children])
		# else:
		# 	structure_s = ""
		s = """
			{0}
				{1} {2}
			{3}
		""".format( ot, self.__contents, structure_s, ct ) # <div>...</div>
		return s


class HtmlPre(HtmlDiv):
	_tag = "pre"


# MAIN
builder = HtmlPageBuilder()

div0 = HtmlDiv()
builder.append(div0)

div1 = HtmlDiv("Hello World")
div0.append(div1)

div2 = HtmlDiv("Hello You")
div0.append(div2)

pre1 = HtmlPre("""This is the "pre" tag.""")
div0.append(pre1)

div0.contents = "Hi ! "

html_code = str(builder)
print(html_code)
with open('exo.html', 'w') as f:
	f.write(html_code)

# <html>
# <head></head>
# <body>
#   <div>
# 		<div>Hello World</div>
# 		<div>Hello You</div>
# 		<pre>This is the "pre" tag.</pre>
#   </div>
# </body>
# </html>

