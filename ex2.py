inTxt = input("Введите список значений через пробел: ")
inVec = inTxt.split(" ")
tempVec = list.copy(inVec)
inVec[1::2] = inVec[:-1:2]
inVec[:-1:2] = tempVec[1::2]
print(inVec)
