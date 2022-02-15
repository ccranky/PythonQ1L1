with open("my_file.txt", "r") as f_obj:
    content = f_obj.readlines()
    print(f"В файле {len(content)} строк.")
    for i, src in enumerate(content, 1):
        word_cntr = len(src.split())
        print(f"В строке {i} - {word_cntr} слов.")