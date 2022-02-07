def myFun(arg1, arg2, arg3):
    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
        arg3 = float(arg3)
    except:
        return "Ошибка! Введены не числа."
    if arg1 < arg2:
        return arg2 + arg3 if arg3 > arg1 else arg1 + arg3
    else:
        return arg1 + arg3 if arg3 > arg2 else arg1 + arg2

print(f" {myFun(input('Введите число № 1: '), input('Введите число № 2: '), input('Введите число № 3: '))}")