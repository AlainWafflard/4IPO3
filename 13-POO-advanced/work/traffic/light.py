class Light:
    def __init__(self, car_o):
        self.car_o = car_o
        self.status = 1   # 1 = rouge, 2 = vert

    def __str__(self):
        return f"Light: {self.status}, following {self.car_o.voiture_name}"

    def change(self):
        self.status = 3 - self.status
        match self.status:
            case 1 :
                self.car_o.stop()
            case 2 :
                self.car_o.start()

