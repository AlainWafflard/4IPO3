from bachelor import Bachelor

class HigherSchool:

    def __init__(self, name):
        self.__name = name
        self.bachelor_d = {}

    def add_bachelor(self, name):
        self.bachelor_d[name] = Bachelor(name)

    def add_course_to_bachelor(self, bach_name, course_name ):
        self.bachelor_d[bach_name].add_course(course_name)

