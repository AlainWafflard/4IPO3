from abc import ABC, abstractmethod


class HtmlObject(ABC):

    def __init__(self, contents=""):
        self.contents = contents
        self.body = []

    @abstractmethod
    def __str__(self):
        pass

    def make_body(self):
        """
        part of __str__() ...
        :return:
        """
        body_s =""
        for o in self.body:
            body_s += str(o)
        return body_s

    def appendElement(self, o):
        self.body.append(o)



