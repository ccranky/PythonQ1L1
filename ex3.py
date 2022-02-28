class myException(Exception):
    def __init__(self, txt, *some_data):
        self.txt = txt

lst = []
while True:
    try:
        a = input("Введите значение: ")
        if "stop" in a:
            break
        if not a.isdigit():
            raise myException("Введено не число!")
    except myException as err:
        print(err)
    else:
        lst.append(a)

print(lst)