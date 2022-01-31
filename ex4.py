inVal = int(input("Enter val: "))
tempVal = 0
while inVal // 10 > 0:
    if (inVal % 10 > tempVal):
        tempVal = inVal % 10
    inVal /= 10
print(f"The biggest number is {int(tempVal)}")