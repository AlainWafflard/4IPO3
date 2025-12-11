from htmlparent import HtmlObject
from htmlpagebuilder import HtmlPageBuilder
from htmldiv import HtmlDiv, HtmlPre, HtmlSection


builder = HtmlPageBuilder()
section = HtmlSection()
builder.appendElement(section)
div1 = HtmlDiv("Hello World")
section.appendElement(div1)
div2 = HtmlDiv("Hello You")
section.appendElement(div2)
pre1 = HtmlPre("""I'm "pre".""")
section.appendElement(pre1)
print(builder)

# o = HtmlObject()

# html_o.appendElement(div_o)
