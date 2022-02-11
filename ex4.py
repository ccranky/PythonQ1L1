inList = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
outList = [el for el in inList if inList.count(el) == 1]
print(*outList)