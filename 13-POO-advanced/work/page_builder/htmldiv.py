from htmlparent import HtmlObject


class HtmlDiv(HtmlObject):
    tag_name = "div"

    def __str__(self):
        body_s = self.make_body()

        return f"""
        <{self.tag_name}>{self.contents}
            {body_s}
        </{self.tag_name}>
        """

class HtmlPre(HtmlDiv):
    tag_name = "pre"


class HtmlSection(HtmlDiv):
    tag_name = "section"


