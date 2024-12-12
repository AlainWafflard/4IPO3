class HtmlPageBuilder:

    def __init__(self):
        self.__element_l = []

    def __str__(self):
        out = """
        <html>
        <head></head>
        <body>
        """
        for o in self.__element_l:
            out += str(o)
        out += """
        </body>
        </html>
        """
        return out

    def append(self, o):
        self.__element_l.append(o)


class HtmlDiv:
    _tagname = "div"

    def __init__(self, content=""):
        self._content = content
        self.__element_l = []

    def __str__(self):
        out = f"<{self._tagname}>"
        out += self._content + "\n"
        for o in self.__element_l:
            out += str(o)
        out += f"</{self._tagname}>\n"
        return out

    def append(self, o):
        self.__element_l.append(o)


class HtmlPre(HtmlDiv):
    _tagname = "pre"


class HtmlSection(HtmlDiv):
    _tagname = "section"


if __name__ == "__main__":
    builder = HtmlPageBuilder()

    section = HtmlSection()
    builder.append(section)

    div1 = HtmlDiv("Hello World")
    section.append(div1)

    div2 = HtmlDiv("Hello You")
    section.append(div2)

    pre1 = HtmlPre("""I'm "pre".""")
    section.append(pre1)

    print(builder)


