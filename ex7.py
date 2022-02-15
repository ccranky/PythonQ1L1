from functools import reduce
import json

with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    vec4 = {x[0]: float(x[2])-float(x[3]) for x in [line.split() for line in f_obj]}
    vec4['average'] = reduce(lambda x, y: x + y if y > 0 else x, vec4.values())
    #vec5 = {k: reduce(lambda x, y: x + y,[float(it[0:it.find("(")]) if "(" in it else 0 for it in val]) for k, val in vec4.items()}
    print(vec4)

with open("text_7.json", "w") as f_obj:
    json.dump(vec4, f_obj)