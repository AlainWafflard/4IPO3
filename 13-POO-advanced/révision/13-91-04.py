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
	_tag = "div"

	def __init__(self, c=""):
		self.__contents = c

	@property
	def contents(self):
		return self.__contents

	@contents.setter
	def contents(self, s):
		self.__contents = s

	def __str__(self):
		ot = "<" + self._tag + ">"  # open tag
		ct = "</" + self._tag + ">" # close tag
		s = ot + self.__contents + ct + "\n" # <div>...</div>
		return s

class HtmlPre(HtmlDiv):
	_tag = "pre"


# MAIN
html_o = HtmlPageBuilder()

div1_o = HtmlDiv("Hello World")
html_o.append(div1_o)

div2_o = HtmlDiv("Hello You")
html_o.append(div2_o)

pre1_o = HtmlPre("""This is the "pre" tag.""")
html_o.append(pre1_o)

print(html_o)

# <html>
# <head></head>
# <body>
# 	<div>Hello World</div>
# 	<div>Hello You</div>
# 	<pre>This is the "pre" tag.</pre>
# </body>
# </html>
