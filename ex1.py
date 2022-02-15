with open("my_file.txt", "a") as f_obj:
    while True:
        some_str = input("Введите данные: ")
        if len(some_str) != 0:
            f_obj.write(some_str + "\n")
        else:
            print("Завершение работы программы")
            break