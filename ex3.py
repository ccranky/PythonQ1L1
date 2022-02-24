class Cell():
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n > other.n:
            return Cell(self.n - other.n)
        else:
            print("Ошибка вычитания")
            return None

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n // other.n)

    def make_order(self, val):
        out_val = ["*" if (i + 1) % val != 0 else "*\n" for i in range(self.n)]
        print(''.join(out_val))


m = Cell(15)
m.make_order(6)
