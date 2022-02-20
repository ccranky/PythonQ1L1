class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = bool(is_police)
    def go(self, speed = 40):
        self.speed = speed
        print(f"Машина {self.name} поехала.")
    def stop(self):
        self.speed = 0
        print(f"Машина {self.name} остановилась.")
    def turn(self, dir):
        print(f"Машина {self.name} повернула " + "направо" if dir else "налево" + ".")
    def show_speed(self):
        print(f"Машина {self.name} движется со скоростью {self.speed}.")

class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)
    def show_speed(self):
        print(f"Машина {self.name} движется со скоростью {self.speed}.")
        if self.speed > 60:
            print(f"Машина {self.name} превышает скорост.")

class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)
    def show_speed(self):
        print(f"Машина {self.name} движется со скоростью {self.speed}.")
        if self.speed > 40:
            print(f"Машина {self.name} превышает скорость.")

class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)
    def show_speed(self):
        print(f"Машина {self.name} движется со скоростью {self.speed}.")

car_1 = WorkCar(50, 'red', 'id1')
car_2 = TownCar(70, 'red', 'id2')
car_3 = SportCar(110, 'blue', 'id3')
car_1.show_speed()
car_3.show_speed()
car_3.turn(True)
#car_2.show_speed()