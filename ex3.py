inVal = input("Enter your value: ")
monthDict = {'1': 'Январь', '2': 'Февраль', '3': 'Март', '4': 'Апрель', '5': 'Май', '6': 'Июнь',
             '7': 'Июль', '8': 'Август', '9': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
monthList = [list(monthDict.keys()), list(monthDict.values())]
print(f"Ваш месяц {monthDict.get(inVal)}")
print(f"Ваш месяц {monthList[1][monthList[0].index(inVal)]}")
