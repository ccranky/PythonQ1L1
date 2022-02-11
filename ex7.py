from functools import reduce

def my_fctr(inVal):
    for i in range(1, inVal+1):
        yield i

val = int(input("Введите целое число: "))
print(f"Факториал числа {val} равен: ", end='')
temp = 1
for el in my_fctr(val):
    temp *= el
    print(f"{el}", end='*')
print(f" ={reduce(lambda x, y: x * y, my_fctr(val))}.")
