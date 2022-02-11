def my_iter_one(arg1, arg2):
    for i in range(arg1, arg2+1):
        yield i

def my_iter_two(inList, cntr):
    i = 0
    while True:
        yield inList[i % len(inList)]
        i += 1
        if i >= cntr:
            return inList[i % len(inList)]


for i in my_iter_one(1, 5):
    print(i)

someList = ["as", 1, 2, 3, 2.12, (1, 2)]
for i in my_iter_two(someList, 5):
    print(i)