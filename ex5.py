class Stationery():
    def __init__(self, title = "Stationery"):
        self.title = title
    def draw(self):
        print("Отрисовка.")

class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручки.")

class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандаша.")

class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркера.")

items = [Pen('Р'), Pencil('К'), Handle('М')]
for i in items:
    i.draw()