from sys import argv

if(len(argv) == 4):
    _, arg1, arg2, arg3 = argv
    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
        arg3 = float(arg3)
        print(f"Заработная плата равна: {arg1 * arg2 + arg3}.")
    except Exception:
        print("Ошибка конвертации")
else:
    print("Ошибка, неверное число аргументов!")