from htmlparent import HtmlObject


class HtmlPageBuilder(HtmlObject):

    def __str__(self):
        body_s = self.make_body()

        return f"""
        <html>
        <head></head>
        <body>
            {body_s}
        </body>
        </html>
        """

