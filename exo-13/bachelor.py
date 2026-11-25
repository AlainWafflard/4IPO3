class Bachelor:

    def __init__(self, name):
        self.__name = name   # "BIG"
        self.course_d = {}

    def add_course(self, course_name):
        self.course_d[course_name] = None
        # XXXXXXXXXXXXXXXXX
