def myFun(inStr):
    strVec = inStr.split(" ")
    sum = 0
    numCntr = 0
    for el in strVec:
        if el.count("&") > 0:
            return sum, numCntr, "Выход"
        if el.isnumeric():
            numCntr += 1
            sum += float(el)
    return sum, numCntr, "Ок"

sum = 0
while True:
    inVal = input("Введите числа через пробел, для выхода введите &: ")
    inSum, inCntr, state = myFun(inVal)
    if state == "Ок":
        sum += inSum
        print(sum)
    elif inCntr > 0:
        sum += inSum
        print(sum)
        print("Завершение работы программы")
        break
    else:
        print("Завершение работы программы")
        break