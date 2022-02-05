inTxt = input("Введите строку: ")
txtVec = inTxt.split(" ")
for i, el in enumerate(txtVec, 1):
    printEl = el[:10] if len(el) > 10 else el
    print(f"{i} {printEl}")
