class Student:
    name = 'unknown'  # class attribute

    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name={}'.format(cls.name))

    @classmethod
    def tostring_with_error(cls):
        print('Student Class Attributes: name={}, age={}'.format(cls.name, cls.age))


if __name__ == "__main__":
    # on appelle la méthode de classe
    Student.tostring()

    # idem mais via un objet
    std = Student()
    std.tostring()
    # std.tostring_with_error()

    # on appelle la méthode de classe => error
    # AttributeError: type object 'Student' has no attribute 'age'
    # ceci parce que self.age est
    # un attribut d'objet, défini dans le constructeur
    # et non un attribut de classe
    Student.tostring_with_error()

