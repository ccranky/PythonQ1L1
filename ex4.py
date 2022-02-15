word_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
             'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'zero': 'ноль'}
with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    f_obj2 = open("text_4_wr.txt", "a", encoding="utf-8")
    content = f_obj.readlines()
    for i in content:
        for k in i.split():
            if str(k).lower() in word_dict:
                f_obj2.write(str(i).replace(k, word_dict.get(str(k).lower())).capitalize())
    f_obj2.close()
