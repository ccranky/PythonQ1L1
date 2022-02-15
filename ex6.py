from functools import reduce

with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    vec4 = {x[0:x.find(":")]: x[x.find(":")+2:-1].split(" ") for x in [line.strip() for line in f_obj]}
    vec5 = {k: reduce(lambda x, y: x + y,[float(it[0:it.find("(")]) if "(" in it else 0 for it in val]) for k, val in vec4.items()}
    print(vec5)