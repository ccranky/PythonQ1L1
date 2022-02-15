from functools import reduce

with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.readlines()
    data = {el[0]: el[1] for el in map(lambda x: x.split(), content)}
    print(f"Средняя зп: {reduce(lambda x, y: float(x)+float(y), list(data.values()))/len(data)}.")
    for i in data.items():
        if float(i[1]) < 20000:
            print(i[0])