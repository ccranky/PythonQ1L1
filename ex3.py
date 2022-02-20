class Worker():
    def __init__(self, name = "NoName", surname = "NoSurname", position = "Position", income = (0, 0)):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income[0], "bonus": income[1]}

class Position(Worker):
    def __init__(self, name = "NoName", surname = "NoSurname", position = "Position", income = (0, 0)):
        Worker.__init__(self, name, surname, position, income)

    def get_full_name(self):
        return self.surname + " " + self.name
    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]

ex = Position("Ivan", "Ivanov", "Manager", (10000, 3000))
print(ex.get_full_name())
print(ex.get_total_income())