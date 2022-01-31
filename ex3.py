inVal = int(input("Enter n: "))
tempVal = inVal
cntr = 1
while tempVal // 10 >= 1:
    cntr += 1
    tempVal /= 10
outVal = inVal * 10 ** cntr + inVal * 10 ** (2 * cntr) + inVal
print(outVal)
