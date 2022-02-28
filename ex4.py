class TechRepo():
    item_number = 0
    total_price = 0
    item_list = {"copy": 0, "printer": 0}

    def add_item(self, item):
        quant = item.quant
        self.item_list[item.type] += quant
        TechRepo.item_number += quant
        TechRepo.total_price += item.price * quant

    def move_item(self, item, val=1):
        quant = val
        if (TechRepo.checkVal(quant)):
            if self.item_list.get(item.type):
                if (self.item_list[item.type] >= quant):
                    self.item_list[item.type] -= quant
                    TechRepo.item_number -= quant
                    TechRepo.total_price -= item.price * quant
                else:
                    TechRepo.item_number -= self.item_list[item.type]
                    TechRepo.total_price -= item.price * self.item_list[item.type]
                    self.item_list[item.type] = 0



    @classmethod
    def get_total_quant(cls):
        return cls.total_price

    def checkVal(quant):
        if not isinstance(quant, int):
            print("Введено неверное количетсво техники!")
            return False
        else:
            return True


class Tech:
    def __init__(self, type, name, price, quant=1):
        self.type = type
        self.name = name
        self.price = price
        self.quantity = quant

    @property
    def quant(self):
        return self.quantity




class Copy(Tech):
    def __init__(self, name, price, num_of_copy, quant=1):
        super().__init__("copy", name, price, quant)
        self.num_of_copy = num_of_copy


class Printer(Tech):
    def __init__(self, name, price, color_type, quant=1):
        super().__init__("printer", name, price, quant)
        self.color_type = color_type


t = TechRepo()
c = Copy("Xerox", 1000, 5000, 10)
p = Printer("HP", 700, 'CMYK', 3)

t.add_item(c)
print(t.total_price)
t.add_item(p)
print(t.total_price)
print(t.item_list)
t.move_item(p, 2)
print(t.total_price)
print(t.item_list)