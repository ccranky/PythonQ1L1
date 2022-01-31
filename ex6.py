debVal = float(input("Enter debit val: "))
credVal = float(input("Enter credit val: "))
if credVal > debVal:
    print("Bad news!")
else:
    print(f"Good news! Profitability is {(debVal - credVal) / debVal}.")
    popVal = int(input("Enter number of employees: "))
    print(f"Profit per employee is {(debVal - credVal) / popVal}.")
