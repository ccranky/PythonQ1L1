def someFun(arg1, arg2):
    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
    except:
        return "Ошибка! Введены не числа"
    try:
        outVal = arg1 / arg2
    except:
        return "Ошибка! Деление на ноль"
    return arg1 / arg2

a = input("Введите число 1: ")
b = input("Введите число 2: ")
print(f"Результат {someFun(a, b)}")