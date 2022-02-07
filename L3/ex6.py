def myFun(inTxt):
    out = inTxt.copy()
    for i, el in enumerate(inTxt):
        out[i] = el.capitalize()
    return " ".join(out)

print(myFun(input("Введите строку: ").split(" ")))
