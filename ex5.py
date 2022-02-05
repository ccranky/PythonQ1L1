startVec = [7, 5, 3]
while True:
    inVal = input("Введите цифру чтобы продолжить или что-то другое для выхода: ")
    if inVal.isnumeric():
        inVal = int(inVal)
        if inVal // 10 == 0:
            for i, el in enumerate(startVec):
                if inVal > el:
                    startVec.insert(i, inVal)
                    print(startVec)
                    break
                elif i == len(startVec)-1:
                    startVec.append(inVal)
                    print(startVec)
                    break
    else:
        break
print(startVec)
