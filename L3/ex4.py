def myFun(arg1, arg2):
    if arg2 == 0:
        return 1
    return (arg1 * myFun(arg1, arg2 - 1) if arg2 > 0 else 1 / arg1 * myFun(arg1, arg2 + 1))


print(myFun(int(input("Введите число: ")), int(input("Введите степень: "))))