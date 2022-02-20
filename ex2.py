class Road():
    def __init__(self, in_length, in_width):
        self.__length = in_length
        self.__width = in_width
    def calc(self):
        return self.__width * self.__length * 25 * 5

ex = Road(1000, 10)
print(ex.calc())