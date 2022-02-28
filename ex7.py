class ComplexNum():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.imag * other.imag,
                          self.imag * other.real + self.real * other.imag)

    def __str__(self):
        return f"Real part: {self.real}, Image part: {self.imag}."


n1 = ComplexNum(2, 3)
n2 = ComplexNum(1, 10)
print(n1 + n2)
print(n1 * n2)
