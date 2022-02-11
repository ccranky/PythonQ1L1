inList = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#outList = (el for el, inEl in list(zip(inList[1:], inList[0:-1])) if el > inEl)
a = tuple(zip(inList[1:], inList[:-1]))
outList = (el for el, inEl in a if el > inEl)

print(*outList)