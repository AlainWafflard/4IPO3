class Car:

    def __init__(self, voiture_name):
        self.voiture_name = voiture_name
        self.status =  False # False = stop ; True = running

    def __str__(self):
        if self.status:
            out = f"{self.voiture_name} : running ..."
        else:
            out =  f"{self.voiture_name} : waiting for the green  light"
        return out

    def start(self):
        self.status = True

    def stop(self):
        self.status = False
