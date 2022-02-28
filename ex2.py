class myException(Exception):
    def __init__(self, txt, *some_data):
        self.txt = txt

try:
    a = input("Введите число, на которое будем делить: ")
    if a.isdigit():
        if int(a) == 0:
            raise myException("Делим на ноль!")
except myException as err:
    print(err)