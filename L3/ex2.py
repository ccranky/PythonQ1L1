def myFun(usName, usFam, usBY, usCity, usEmail, usPhone):
    return f"Фамилия: {usFam}, Имя: {usName}, Год рождения: {usBY}, \
Город: {usCity}, Эл. почта: {usEmail}, Телефон: {usPhone}"

print(myFun(
    usFam=input("Введите фамилию: "), usName=input("Введите имя: "),
    usCity=input("Введите город: "), usEmail=input("Введите адрес электронной почты:"),
    usPhone=input("Введите телефон: "), usBY=input("Введите год рождения: ")))