firstDayVal = float(input("Enter first day value: "))
goalVal = float(input("Enter goal value: "))
cntr = 1
while firstDayVal < goalVal:
    firstDayVal *= 1.1
    cntr += 1
print(f"Happy day: {cntr}")
