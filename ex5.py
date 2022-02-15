import random
from functools import reduce

var_list = [str(random.randint(1, 100)) for x in range(1, 10)]
print(' '.join(var_list))
with open("text_5.txt", "w", encoding="utf-8") as f_obj:
    f_obj.write(' '.join(var_list))
with open("text_5.txt", "r", encoding="utf-8") as f_obj:
    m2 = reduce(lambda x, y: int(x)+int(y), [line.strip().split() for line in f_obj][0])
    print(m2)