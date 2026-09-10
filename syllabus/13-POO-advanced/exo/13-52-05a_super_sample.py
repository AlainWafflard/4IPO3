# Example of super()

class Company:
    __name = "Google"

    def company_name(self):
        return 'Google'

class Department(Company):
    __name = "Sales"

    def info(self):
        # Calling the superclass method using super()function
        d_name = self.__name
        c_name = super().company_name()
        print("{} is a department of {}".format(d_name, c_name))


# Creating object of child class
dep = Department()
dep.info()


